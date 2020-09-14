## korean_language_competition_2020

### ★★ pip install -r requirements.txt ★★★


#### data 폴더 --> (train, dev, test) 데이터 


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
    

### language_model.py
os.environ["CUDA_VISIBLE_DEVICES"] ='2' --> 2번째 GPU를 사용 --> 몇번째 GPU를 사용할 것인지 변경하기 
#### 실행방법 : python run_language_modeling.py
                --model_name_or_path model_name
                --do_train
                --train_data_file = inputFile.txt
                --mlm
                --line_by_line
                --output_dir outPutDir
                --tokenizer_name tokenizerName
                --num_train_epochs = 4
                --logging_steps 500
                --save_steps 27985



### run_Kobert.py ==> KoBert 실행
os.environ["CUDA_VISIBLE_DEVICES"] ='2' --> 2번째 GPU를 사용 --> 몇번째 GPU를 사용할 것인지 변경하기
#### 실행 방법 : python run_Kobert.py 
                 --model_name_or_path monologg/kobert
                 --task_name SST-2
                 --do_train
                 --do_eval
                 --data_dir ./data
                 --max_seq_length 256
                 --per_device_eval_batch_size=32
                 --per_device_train_batch_size=32
                 --learning_rate 3e-5
                 --num_train_epochs 4.0
                 --output_dir ./run_glue_result/kobert
                 --do_predict
                 --save_steps 59460
                 --tokenizer_name monologg/kobert
                 
### run_bert.py ==> 1)BERT 실행 2)korElectra
os.environ["CUDA_VISIBLE_DEVICES"] ='2' --> 2번째 GPU를 사용 --> 몇번째 GPU를 사용할 것인지 변경하기
                 --model_name_or_path modelName
                 --task_name SST-2
                 --do_train
                 --do_eval
                 --data_dir ./data
                 --max_seq_length 256
                 --per_device_eval_batch_size=32
                 --per_device_train_batch_size=32
                 --learning_rate 3e-5
                 --num_train_epochs 4.0
                 --output_dir ./run_glue_result/modelName
                 --do_predict
                 --save_steps 59460
