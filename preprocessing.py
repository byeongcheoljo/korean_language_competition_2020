import re
import sys
from soynlp.normalizer  import repeat_normalize, emoticon_normalize, only_hangle
import pandas as pd
import numpy as np
import random
import time
import datetime
import emoji
import csv

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

file_name = sys.argv[1]
naver_data = pd.read_csv(file_name, sep="\t")
naver_doc = naver_data['document'].values
naver_rating  = naver_data['label'].values


sentences = []
ratings = []
for naver_review, naver_rate in zip(naver_doc, naver_rating):
    try:
        naver_review = clean(naver_review)
        naver_review = repeat_normalize(naver_review, num_repeats = 2)
        naver_review = emoticon_normalize(naver_review)
        naver_review = only_hangle(naver_review)

        if len(naver_review) >= 4:
            sentences.append(naver_review)
            ratings.append(naver_rate)
    except:
        pass

with open(file_name+"preprocessing.tsv", 'w') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for sent, rate in zip(sentences, ratings):
        tsv_writer.writerow([sent, rate])
