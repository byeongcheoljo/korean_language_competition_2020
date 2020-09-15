#### 모델의 최고 성능은 6개의 모델을 앙상블 했을 때지만 시간 효율을 고려해 단일 모델 중 최고 성능인 모델로 Predict 진행  

### 테스트 파일 실행 방법  
     1. Dockerfile이 있는 폴더로 이동  
  
     2. docker build --tag [이미지 이름] .  
  
        ex) docker build --tag tmp_image .  
  
     3. docker run -i -t --name [컨테이너 이름] [이미지 이름]  
  
        ex) docker run -i -t --name tmp_container tmp_image
  
     현재 /workspace/Competition 폴더 안에 있는지 확인!!
  
     4. python preprocessing.py $dataFile
  
        ex) python preprocessing.py data.tsv
  
     5. python sentiment_predict.py argument.json
  
     이후 result/ 폴더 아래에 결과(test_results_sentiment.txt) 생성
  
  
### 주의할 점
     
   preprocessing.py 실행시에 argument로 입력하는 $dataFile 의 경우 반드시 id column이 존재하는 nsmc 데이터 형식을 가질 것. (구분자 '\t')
  
     -----------------가능한 형식----------------------
     id document  label  
     1  재미있는 영화입니다. 1  
     2  재미없는 영화입니다. 0
     
     id sentence
     1  재미있는 영화입니다.
     2  재미없는 영화입니다.
     
     
     -----------------불가능한 형식----------------------
     sentence label
     재미있는 영화입니다.  1
     재미없는 영화입니다.  0
     
     document
     재미있는 영화입니다.
     재미없는 영화입니다.

