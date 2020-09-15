## korean_language_competition_2020

### ★ 학습 된 모델을 테스트할 시 Docker를 사용해주세요. docker폴더에 들어가 README를 참고해주세요.★  


#### ※ 학습 방법은 아래를 참고해주세요.
### pip install -r requirements.txt 

### data 폴더 - (train, dev, test)


###  크롤링 - watcha_link_list.py  
#### 실행방법: python watcha_link_list.py   
#### 왓챠 회원가입 후 ID와 Password 입력    
    watcha_email = "id"
    
    password = 'password'
    
#### Chrome Web Driver 다운 
    chrome://version/ 여기에 접속 후 Chrome version 확인
    https://sites.google.com/a/chromium.org/chromedriver/downloads 크롬과 동일한 버전 download 
    driver = webdriver.Chrome("chromedriver_win32/chromedriver") --> 코드에 경로 적용

### 데이터 전처리 및 분리 - train_dev_test_dataSplit_data_preprocessing.py
#### 실행 방법: python train_dev_test_dataSplit_data_preprocessing.py
    크롤링으로 watcha 데이터를 수집하면 "./nsmc/watcha_review_concat.xlsx" 경로에 저장하거나 코드 수정 

    nsmc데이터와 watcha데이터를 합친 후 전처리(정제)
    
    랜덤하게 데이터를 shuffle 후 train, dev, test 데이터로 분리
    
    ./data/train.tsv, ./data/dev.tsv, ./data/test.tsv 파일 생성 --> resultFile
    
## ★데이터 전처리 및 분리 과정을 통해 실험을 진행하였지만, 대회측에서는 preprocessing.py을 통해 전처리 과정을 해주시길 바랍니다.★
#### 실행방법: python preprocessing.py fileName 
#### outputFile : fileName.preprocessing.tsv


#### 국립국어원 모두의 말뭉치 전처리 (국립국어원 신문 말뭉치(버전1.0), 국립국어원 웹 말뭉치(버전 1.0)사용)
    실행 코드: modu_convert.ipynb 


### language_model.py

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
                 
### run_bert.py ==> 1)BERT 실행 2)koElectra
 
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
    
    
### run_glue_result 폴더 : 자체 실험을 통한 각 모델들 결과 폴더 입니다.
    run_glue_result/kobert/test_results_sst-2.txt : kobert
    run_glue_result/kobert_languagemodel/test_results_sst-2.txt : kobert language model fine-tuning
    run_glue_result/koelectra_base_discriminator/test_results_sst-2.txt : koelectra
    run_glue_result/koelectra_languagemodel/test_results_sst-2.txt : koelectra language model fine-tuning
    run/glue_result/sentiment_bert_base_multilingual/test_results_sst-2.txt : BERT
    
    
### sentiment_result_combination.py
    run_glue_result 폴더 결과들을 불러들여와 단일 모델 및 앙상블 모델 결합 후 결과를 출력하는 파일입니다.
    
#### References:  
https://github.com/huggingface/pytorch-transformers  
https://github.com/e9t/nsmc  
https://github.com/monologg/KoELECTRA  
https://github.com/SKTBrain/KoBERT  
https://pedia.watcha.com/ko-KR/

