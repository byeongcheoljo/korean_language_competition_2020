## korean_language_competition_2020

### watcha_link_list.py
#### python watcha_link_list.py 실행
#### 왓챠 ID와 Password 입력    
    watcha_email = "id"
    
    password = 'password'
#### Chrome Web Driver 다운 
    chrome://version/ 여기에 접속 후 Chrome version 확인
    https://sites.google.com/a/chromium.org/chromedriver/downloads 크롬과 동일한 버전 download 
    driver = webdriver.Chrome("D:/다운로드/chromedriver_win32/chromedriver") --> 코드에 적용


### train_dev_test_dataSplit_data_preprocessing.py
#### 실행 방법: python train_dev_test_dataSplit_data_preprocessing.py
    nsmc데이터와 watcha데이터를 합친 후 전처리(정제)
    
    랜덤하게 데이터를 shuffle 후 train, dev, test 데이터로 분리
    
    ./data/train.tsv, ./data/dev.tsv, ./data/test.tsv 파일 생성 --> resultFile
    
