from itertools import combinations


def sum_avg_probability(y_pro_list):
    file_length = len(y_pro_list)
    length_file_list = len(y_pro_list[0])

    sumProbability = []
    avgProbability = []
    for i in range(length_file_list):
        temp = 0
        for k in range(len(y_pro_list)):
            temp += y_pro_list[k][i]
        sumProbability.append(temp)
        avgProbability.append(temp/file_length)
        # print(sumProbability)
    return sumProbability, avgProbability

def calculateAcc(y_0_sumOrAvg_result_list, y_1_sumOrAvg_result_list, original_testFile):
    correct_answer = []
    for ln in open(original_testFile):
        line = ln.strip().split('\t')
        try:
            prediction = int(line[2])
            correct_answer.append(prediction)
        except:
            pass


    y_predict_list = []
    for y0_sumOravg_result, y1_sumOravg_result in zip(y_0_sumOrAvg_result_list, y_1_sumOrAvg_result_list):
        if y0_sumOravg_result >= y1_sumOravg_result:
            y_predict_list.append(0)
        else:
            y_predict_list.append(1)


    total_count = len(y_predict_list)
    count = 0
    for y, y_pred in zip(correct_answer, y_predict_list):
        if  y == y_pred:
            count +=1
    # print(count)

    return (float(count)/float(total_count))*100


result_index = [0,1,2,3,4,5]
# result_index = [0,1,2]
result_dir = './run_glue_result/'
file_result_list = [result_dir+'kobert/test_results_sst-2.txt',result_dir+'koelectra_base_discriminator/test_results_sst-2.txt',result_dir+'sentiment_bert_base_multilingual/test_results_sst-2.txt',
result_dir+"koelectra_languagemodel/test_results_sst-2.txt", result_dir+"kobert_languagemodel_news_review/test_results_sst-2.txt", result_dir+"bert_multilingual_lm/test_results_sst-2.txt"]
total_combi = []
for i in range(len(result_index)):
    combi = combinations(result_index, i+1)
    combi_result = (list(combi))
    for i in combi_result:
        total_combi.append(list(i))

total_combi_result = total_combi
print(total_combi_result)
# print(type(total_combi_result[0][0]))





for listIndex in total_combi_result:
    y_0_pro_list =[]
    y_1_pro_list = []
    for index in listIndex:
        print(file_result_list[index].split("/")[-2])
    # for file_name in file_result_list:
        y_0_pro = []
        y_1_pro = []
        for ln in open(file_result_list[index]):
            line = ln.strip().split("\t")
            try:
                y_0 = float(line[2])
                y_1 = float(line[3])
            except:
                y_0 = str(line[2])
                y_1 = str(line[3])

            y_0_pro.append(y_0)
            y_1_pro.append(y_1)
        y_0_pro.pop(0)
        y_1_pro.pop(0)
        y_0_pro_list.append(y_0_pro)
        y_1_pro_list.append(y_1_pro)



    y_0_sum_result_list, y_0_avg_result_list = sum_avg_probability(y_0_pro_list)
    y_1_sum_result_list, y_1_avg_result_list = sum_avg_probability(y_1_pro_list)
    # print(y_0_sum_result_list[0:10])
    # print(y_0_sum_result_list[0:10])


    # print(len(y_0_sum_result_list), len(y_0_avg_result_list))
    # print(len(y_1_sum_result_list), len(y_1_avg_result_list))



    a = calculateAcc(y_0_sum_result_list, y_1_sum_result_list, "./sentiment_tsv_data/test3.tsv")
    b = calculateAcc(y_0_avg_result_list, y_1_avg_result_list, "./sentiment_tsv_data/test3.tsv")
    print(a)
    # print(b)
