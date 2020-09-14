## korean_language_competition_2020

### watcha_link_list.py
#### 왓챠 ID와 Password 입력후 python watcha_link_list.py 실행
    watcha_email = "id"
    password = 'password'


### train_dev_test_dataSplit_data_preprocessing.py
#### 실행 방법: python train_dev_test_dataSplit_data_preprocessing.py
    nsmc데이터와 watcha데이터를 합친 후 전처리(정제)
    랜덤하게 데이터를 shuffle 후 train, dev, test 데이터로 분리
    ./data/train.tsv, ./data/dev.tsv, ./data/test.tsv 파일 생성 --> resultFile
    
