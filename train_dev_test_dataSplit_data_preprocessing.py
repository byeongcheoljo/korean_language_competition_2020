import sys
import pandas as pd
import random
from soynlp.normalizer  import repeat_normalize, emoticon_normalize, only_hangle
import csv
import emoji
import re

emojis = ''.join(emoji.UNICODE_EMOJI.keys())
pattern = re.compile(f'[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-힣{emojis}]+')
url_pattern = re.compile(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def clean(x):
    x = pattern.sub(' ', x)
    x = url_pattern.sub('', x)
    x = emoji_pattern.sub('',x)
    x = x.strip()
    x = repeat_normalize(x, num_repeats=2)
    x = emoticon_normalize(x)
    return x


random.seed(42)

naver_data = pd.read_csv("nsmc/ratings.txt", sep="\t")
naver_doc = naver_data['document'].values
naver_rating  = naver_data['label'].values
print(naver_rating)


file_name = "./nsmc/watcha_review_concat.xlsx"
read_file = pd.read_excel(file_name)
read_file = read_file.dropna(axis=0)

print(read_file.head())

review_sentence = read_file['review'].values
review_ratings = read_file['rating'].values
assert len(review_sentence) == len(review_ratings), "dose not match length (review, rating)"

sentences = []
ratings = []
for review, rating, naver_review, naver_rate in zip(review_sentence, review_ratings, naver_doc, naver_rating):
    try:
        naver_review = clean(naver_review)
        review = clean(review)
        if len(naver_review) > 4:
            sentences.append(naver_review)
            ratings.append(naver_rate)

        if len(review) > 4 and float(rating) >= 4.0 or float(rating) <= 2.5:
            sentences.append(review)
            if float(rating) >= 4.0:
                ratings.append(1)
            elif float(rating) <= 2.5:
                ratings.append(0)
    except:
        pass


print(sentences[0:5])
print(ratings[0:5])
combine = list(zip(sentences, ratings))
random.shuffle(combine)

sentences, ratings = zip(*combine)
sentences = list(sentences)
ratings = list(ratings)
print(sentences[0:5])
print(ratings[0:5])
print(len(sentences),"\t",len(ratings))


result_list = []
for sent, rate in zip(sentences, ratings):
    str(sent).replace("\t"," ")
    result = str(sent)+"\t"+str(rate)
    result_list.append(result)

train_file = result_list[0:int(len(result_list)*0.9)]
dev_file = result_list[int(len(result_list)*0.9*0.8):int(len(result_list)*0.9)]
test_file = result_list[int(len(result_list)*0.9):]

def save_tsv(file, file_name):
    with open('./data/'+str(file_name)+'3.tsv', 'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['index','sentence','label'])
        for index,file_split in enumerate(file):
            try:
                sentence, label = file_split.strip().split("\t")
                # sentence = sentence_label_split[0].strip()
                # label = sentence_label_split[-1].strip()
                tsv_writer.writerow([index,sentence, label])
            except:
                pass

save_tsv(train_file, "train")
save_tsv(dev_file, "dev")
save_tsv(test_file, "test")

def resave(file,file_name):
    cnt  = 1
    with open('./data/'+(file), 'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for ln in open(file_name):
            try:
                line = ln.strip().split("\t")
                cnt += 1
                # print(line[0],line[1], cnt)
                tsv_writer.writerow([line[1], line[2]])
            except:
                pass

resave("train.tsv","./data/train3.tsv")
resave("dev.tsv","./data/dev3.tsv")
resave("test2.tsv","./data/test3.tsv")

def testDataResave(file,file_name):
    cnt  = 1
    with open('./data/'+(file), 'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for ln in open(file_name):
            try:
                line = ln.strip().split("\t")
                # print(line[0],line[1], cnt)
                tsv_writer.writerow([line[0], line[1]])
            except:
                pass
testDataResave("test2.tsv","./data/test3.tsv")
