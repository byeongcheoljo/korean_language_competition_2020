from bs4 import BeautifulSoup
from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(1)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags(ios)
        u"\U00002702-\U000027B0"
        # u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

## 첫번째 크롤링
href_link = ['https://pedia.watcha.com/ko-KR/contents/tlnN9ov','https://pedia.watcha.com/ko-KR/contents/tlGNOmp','https://pedia.watcha.com/ko-KR/contents/tlAnA7Z',
'https://pedia.watcha.com/ko-KR/contents/tEm9mkr','https://pedia.watcha.com/ko-KR/contents/tE156Wg','https://pedia.watcha.com/ko-KR/contents/tR7WDAR',
'https://pedia.watcha.com/ko-KR/contents/tPVdNjq','https://pedia.watcha.com/ko-KR/contents/tPeWzyB','https://pedia.watcha.com/ko-KR/contents/tlGNQB7',
'https://pedia.watcha.com/ko-KR/contents/tRNADzE','https://pedia.watcha.com/ko-KR/contents/tE0m4p6','https://pedia.watcha.com/ko-KR/contents/tEKYWbV',
'https://pedia.watcha.com/ko-KR/contents/tPrzdaO','https://pedia.watcha.com/ko-KR/contents/tR2ewJW','https://pedia.watcha.com/ko-KR/contents/tRBxA7l',
'https://pedia.watcha.com/ko-KR/contents/tRNJq9R','https://pedia.watcha.com/ko-KR/contents/tRB0Xql','https://pedia.watcha.com/ko-KR/contents/tPJZQ9K',
'https://pedia.watcha.com/ko-KR/contents/tEmv4dR','https://pedia.watcha.com/ko-KR/contents/tlnMV5P',
'https://pedia.watcha.com/ko-KR/contents/tEKzjp2','https://pedia.watcha.com/ko-KR/contents/tPvZzJZ','https://pedia.watcha.com/ko-KR/contents/tPdYAkl',
'https://pedia.watcha.com/ko-KR/contents/tR7pwnP','https://pedia.watcha.com/ko-KR/contents/tR28Vvl',
'https://pedia.watcha.com/ko-KR/contents/tRzgyLP','https://pedia.watcha.com/ko-KR/contents/tlGA17R',
'https://pedia.watcha.com/ko-KR/contents/t1lGvBP','https://pedia.watcha.com/ko-KR/contents/tPVyY4R','https://pedia.watcha.com/ko-KR/contents/tlxkdvn',
'https://pedia.watcha.com/ko-KR/contents/tRW02NP','https://pedia.watcha.com/ko-KR/contents/tEKMQQP','https://pedia.watcha.com/ko-KR/contents/tPypm4R',
'https://pedia.watcha.com/ko-KR/contents/tRW02DP','https://pedia.watcha.com/ko-KR/contents/tRamVQR','https://pedia.watcha.com/ko-KR/contents/tE3DZmR',
'https://pedia.watcha.com/ko-KR/contents/m5mY6jj', 'https://pedia.watcha.com/ko-KR/contents/m5nXQG9','https://pedia.watcha.com/ko-KR/contents/m5QA6GD',
'https://pedia.watcha.com/ko-KR/contents/mOkLvkQ', 'https://pedia.watcha.com/ko-KR/contents/mW4L2XW', 'https://pedia.watcha.com/ko-KR/contents/mdR4J1L',
'https://pedia.watcha.com/ko-KR/contents/m5mY1nD', 'https://pedia.watcha.com/ko-KR/contents/mWqv6lO', 'https://pedia.watcha.com/ko-KR/contents/m5XKqgp',
'https://pedia.watcha.com/ko-KR/contents/mdKD21k', 'https://pedia.watcha.com/ko-KR/contents/mdMRgzR', 'https://pedia.watcha.com/ko-KR/contents/mdj24Aa',
'https://pedia.watcha.com/ko-KR/contents/m53m2Yn', 'https://pedia.watcha.com/ko-KR/contents/m5ewr3z', 'https://pedia.watcha.com/ko-KR/contents/m5x1Mex',
'https://pedia.watcha.com/ko-KR/contents/mMO2JAO', 'https://pedia.watcha.com/ko-KR/contents/m5NnN08', 'https://pedia.watcha.com/ko-KR/contents/m53mE1y',
'https://pedia.watcha.com/ko-KR/contents/mOgjPj9', 'https://pedia.watcha.com/ko-KR/contents/m53mYnw', 'https://pedia.watcha.com/ko-KR/contents/mdB7vRk',
'https://pedia.watcha.com/ko-KR/contents/mWw3Bq3', 'https://pedia.watcha.com/ko-KR/contents/m5r3607', 'https://pedia.watcha.com/ko-KR/contents/m53m2Zw',
'https://pedia.watcha.com/ko-KR/contents/mOkLpok', 'https://pedia.watcha.com/ko-KR/contents/mWyJbEk', 'https://pedia.watcha.com/ko-KR/contents/mOVvVyp',
'https://pedia.watcha.com/ko-KR/contents/m1WwY4d', 'https://pedia.watcha.com/ko-KR/contents/mOVPpeR', 'https://pedia.watcha.com/ko-KR/contents/m5YKZzw',
'https://pedia.watcha.com/ko-KR/contents/m6dR6gd', 'https://pedia.watcha.com/ko-KR/contents/mVWzX9d', 'https://pedia.watcha.com/ko-KR/contents/mOAgMa5',
'https://pedia.watcha.com/ko-KR/contents/m5aVeGW', 'https://pedia.watcha.com/ko-KR/contents/mW9zVlO', 'https://pedia.watcha.com/ko-KR/contents/mWpBj4d',
'https://pedia.watcha.com/ko-KR/contents/mO09Exd', 'https://pedia.watcha.com/ko-KR/contents/m5m1N75', 'https://pedia.watcha.com/ko-KR/contents/mMO2axW',
"https://pedia.watcha.com/ko-KR/contents/bovqN1L",'https://pedia.watcha.com/ko-KR/contents/boO5akr','https://pedia.watcha.com/ko-KR/contents/b9JMw8M',
'https://pedia.watcha.com/ko-KR/contents/b9nDdXx', 'https://pedia.watcha.com/ko-KR/contents/boNLPM9','https://pedia.watcha.com/ko-KR/contents/b9W08lp',
'https://pedia.watcha.com/ko-KR/contents/b9rgnrg', 'https://pedia.watcha.com/ko-KR/contents/b4Mb2WE', 'https://pedia.watcha.com/ko-KR/contents/b42qe2d',
'https://pedia.watcha.com/ko-KR/contents/b4Mb2ek','https://pedia.watcha.com/ko-KR/contents/bo6bzgB', 'https://pedia.watcha.com/ko-KR/contents/byLaea9',
'https://pedia.watcha.com/ko-KR/contents/b9JMKPM', 'https://pedia.watcha.com/ko-KR/contents/bX9Rlop', 'https://pedia.watcha.com/ko-KR/contents/bokNjW4',
'https://pedia.watcha.com/ko-KR/contents/bolJ0A2', 'https://pedia.watcha.com/ko-KR/contents/boAXz2Y', 'https://pedia.watcha.com/ko-KR/contents/boNvGQo',
'https://pedia.watcha.com/ko-KR/contents/b98KJPV', 'https://pedia.watcha.com/ko-KR/contents/byzNGWy', 'https://pedia.watcha.com/ko-KR/contents/byKmEW4',
'https://pedia.watcha.com/ko-KR/contents/b140l4Z', 'https://pedia.watcha.com/ko-KR/contents/b4MbMqG', 'https://pedia.watcha.com/ko-KR/contents/byEkjG4',
'https://pedia.watcha.com/ko-KR/contents/bymB5Y5', 'https://pedia.watcha.com/ko-KR/contents/b4MbNmk',
'https://pedia.watcha.com/ko-KR/contents/b9xDKa9', 'https://pedia.watcha.com/ko-KR/contents/byKmZ00', 'https://pedia.watcha.com/ko-KR/contents/boYd5PB',
'https://pedia.watcha.com/ko-KR/contents/byVZvvy', 'https://pedia.watcha.com/ko-KR/contents/byKjz0o', 'https://pedia.watcha.com/ko-KR/contents/b9bpODo',
'https://pedia.watcha.com/ko-KR/contents/b405ZEo', 'https://pedia.watcha.com/ko-KR/contents/b9x25Vo', 'https://pedia.watcha.com/ko-KR/contents/bopPDwo',
'https://pedia.watcha.com/ko-KR/contents/byaELDy', 'https://pedia.watcha.com/ko-KR/contents/byav7W0','https://pedia.watcha.com/ko-KR/contents/b40YEEo',
'https://pedia.watcha.com/ko-KR/contents/b4Q50XA', 'https://pedia.watcha.com/ko-KR/contents/bovXK89',
'https://pedia.watcha.com/ko-KR/contents/mWJwrMO','https://pedia.watcha.com/ko-KR/contents/mW9xB85','https://pedia.watcha.com/ko-KR/contents/mJO1Zyd',
'https://pedia.watcha.com/ko-KR/contents/mdRL4bW', 'https://pedia.watcha.com/ko-KR/contents/mO8joj5', 'https://pedia.watcha.com/ko-KR/contents/mWvpJ0d',
'https://pedia.watcha.com/ko-KR/contents/mOlYvyd', 'https://pedia.watcha.com/ko-KR/contents/mdBzNnP', 'https://pedia.watcha.com/ko-KR/contents/m5nQrpo',
'https://pedia.watcha.com/ko-KR/contents/mWpmGjx', 'https://pedia.watcha.com/ko-KR/contents/mdBzrpD', 'https://pedia.watcha.com/ko-KR/contents/m5XMeBW',
'https://pedia.watcha.com/ko-KR/contents/mBOkBwW', 'https://pedia.watcha.com/ko-KR/contents/mW9208O', 'https://pedia.watcha.com/ko-KR/contents/mdBzQED',
'https://pedia.watcha.com/ko-KR/contents/mP5mQx5', 'https://pedia.watcha.com/ko-KR/contents/md7ZPBO', 'https://pedia.watcha.com/ko-KR/contents/mdjlyzW',
'https://pedia.watcha.com/ko-KR/contents/mOo10m5', 'https://pedia.watcha.com/ko-KR/contents/mWvkKMO', 'https://pedia.watcha.com/ko-KR/contents/m5rwLXm',
'https://pedia.watcha.com/ko-KR/contents/m5mGVzO', 'https://pedia.watcha.com/ko-KR/contents/mOo1Zv5', 'https://pedia.watcha.com/ko-KR/contents/mAOlrN5',
'https://pedia.watcha.com/ko-KR/contents/m5Y6qlW', 'https://pedia.watcha.com/ko-KR/contents/mdjal9O', 'https://pedia.watcha.com/ko-KR/contents/m1d6gq5',
'https://pedia.watcha.com/ko-KR/contents/mdjwRxl', 'https://pedia.watcha.com/ko-KR/contents/mOo0wJk', 'https://pedia.watcha.com/ko-KR/contents/mOAGRDl',
'https://pedia.watcha.com/ko-KR/contents/mdjwRKw']

url = "https://pedia.watcha.com/ko-KR"

driver = webdriver.Chrome("D:/다운로드/chromedriver_win32/chromedriver")
driver.implicitly_wait(10)
driver.get(url)
login = driver.find_element_by_class_name("css-jt7ti-StylelessButton-LoginButton")
login.click()

watcha_email = "id" ##왓챠 아이디
password = 'password'## 왓챠 패스워드
copy_input('//*[@id="sign_in_email"]', watcha_email)
time.sleep(1)
copy_input('//*[@id="sign_in_password"]', password)
time.sleep(1)
login_submit = driver.find_element_by_class_name('css-tfr7ty-StylelessButton-Button-LoginButton').click()
time.sleep(3)

num = 1000
review_list = []
rate_list = []
for link in href_link:
    url  = ""
    url = link + '/comments/'
    driver.get(url)
    body = driver.find_element_by_css_selector('body')
    for i in range(num): #num번
        body.send_keys(Keys.PAGE_DOWN) # 페이지 다운 키를  num회 반복한다.
        time.sleep(1) # 페이지 로드 대기

    # beautifulsoup 사용 하기 준비
    html = driver.page_source # html을 문자열로 가져온다.
    # driver.close() # 크롬드라이버 닫기
    soup = BeautifulSoup(html,'html.parser')
    context_list = soup.select("div.css-aintwb-Text")
    rating_list = soup.select("div.css-1a97064-UserActionStatus")

    for context, rating in zip(context_list, rating_list):
        if not "보는중" in rating.find("span").text and not "보고싶어요" in rating.find("span") and not "읽는중" in rating.find("span") and not "읽고싶어요" in rating.find("span"):
            print(emoji_pattern.sub("",context.find('span').text).replace("\n"," "), rating.find("span").text)
            review_list.append(emoji_pattern.sub("",context.find('span').text).replace("\n"," "))
            rate_list.append(rating.find("span").text)
    time.sleep(3)
review_rating = {"review": review_list, "rating" : rate_list}
# total = title_content_answer
pd_test = pd.DataFrame(review_rating)
pd_test.to_csv("watcha_BookAndMovie.csv",encoding='utf-8-sig')
