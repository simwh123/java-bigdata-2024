# file: p31_externalLib.py
# desc: 외부라이브러리 사용법

# > pip install LibName   외부라이브러리 설치
# Successfully installed / Requirement already satisfied 설치 완료시 이 문구가 나와야함
# > pip uninstall LibName  외부라이브러리 삭제
# Successfully uninstalled 설치 삭제시 이 문구가 나와야함

from faker import Faker

dummy = Faker('ko-KR') # 한국어 설정

dummyData = [(dummy.profile()) for _ in range(10)]
#print(dummyData)

## urllib3 외부 웹페이지 분석 모듈

import requests
from bs4 import BeautifulSoup

#res = requests.get('https://www.naver.com')
#print(res.status_code)
#print(res.content) # 내용가져오기

res = requests.get('https://www.google.com/')

if res.status_code == 200:
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    print(soup)