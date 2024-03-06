# java-bigdata-2024
빅데이터 자바 개발자 파이썬 학습 리포지토리

## 1일차

- 파이썬 개발환경
  
    [깃헙](https://github.com)

    [깃설치](https://git-scm.com/download/win)

    [깃헙 데스크탑 설치](https://desktop/github.com)

    [파이썬 설치](https://python.org/)

    [Visual](https://code.visualstudio.com/)

    [나눔고딕코딩](https://github.com/naver/nanumfont)

- 파이썬 학습

    - 파이썬 개요
     
        - 1990년 네덜란드 개발자 귀도 반 로섬이 개발
          쉽고 간결한 문법, 무료, 빠른 개발속도

    - 파이썬 기초문법

        - 숫자형(정수, 실수, 진수)          
   
            변수만 선언, 값만 할당하면 숫자형으로 지정
            C,C++,Java,C 처럼 형지정이 없음
    

        - 문자열형(연산, 문자열 포맷, 함수)
    
            '', "" 모두 사용 가능
    
                
        - 리스트형, 튜플형(연산, 함수)
            리스트는 수정, 삭제 가능
            튜플은 수정, 삭제 불가 그 외는 리스트와 동일

## 2일차

- 파이썬 학습

    - 파이썬 기초문법

        - 딕셔너리, 집합
       
        - 불형

        - None형

        - 제어문 (if, for, while)

        - 제어문 연습

        - 함수(한번 이상 사용하면 함수로 만들어라)
        
        

## 3일차

- 파이썬 학습

    - 파이썬 기초문법
            
        - 화면 입출력
            
        - 파일 입출력
            
        - 프로그램 입출력
            
        - 객체지향

        - 모듈, 패키지

        - 예외처리, 디버깅
        

## 4일차

- 파이썬 학습

    - 파이썬 기초문법

        - 모듈, 패키지

        - ★★예외처리, 디버깅
            
        - 내장 함수
            
        - 표준 라이브러리
            
        - 외부 라이브러리

## 5일차

- 파이썬 학습

    - 파이썬 응용

        - OS 디렉토리

        - 아스키 및 유니코드

        - 주소록 앱 만들기



    ![주소록앱](https://github.com/simwh123/java-bigdata-2024/blob/main/images/day05Test.gif)

            - Windows App 만들기(PyQt 5)

    ![QtApp](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata02.png)

## 6일차
- 파이썬 학습
  - PyQt5 학습
    - Qwidget 자식 클래스 종류 학습

        ![QLabel](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata03.png)

    - Naver 뉴스API 검색 앱

        ![naverApp](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata04.png)

## 7일차
- 파이썬 학습
    - PyQt5 계속
      - Naver 뉴스API 검색 앱 마무리
    - json 학습
    - PyQt5
      - 스레드 개념, 학습

        ![스레드](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata05.png)

- 파이썬 응용
    - TTS(Text To Speech)
    - QRCode 생성기

      ![QR코드생성기](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata06.png)

    - 구글 번역기

      ![구글번역](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata07.png)

## 8일차
- 파이썬 응용
  - PyAutoGui 모듈(마우스, 키보드, 화면캡처)
  - 슬랙 webhook로 모바일 메시지 전송
  - Tesseract 프로그램으로 이미지에서 글자 추출(인식률을 높이려면 직접 트레이닝을 해서 트레이닝 데이터를 만들어야함)


## 9일차
- 파이썬 응용
  - 이미지 처리 OpenCV
    ![그림에디터](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata09.png)
  
  - Flask, Django 웹서버
   
    [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/index.html)

    [Django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django)

  - 그림에디터 만들기
   
    ![그림에디터](https://github.com/simwh123/java-bigdata-2024/blob/main/images/bigdata08.png)
 
 ## 10일차
 - 파이썬 응용
   - 그림에디터 완성(Opencv 그레이스케일)
       - mp4로 동영상 업로드 하려면 github 사이트에서 Readme.md를 수정 클릭 후, mp4를 드래그해서 입력가능
       - 제한사항은 10MB 이하

   - 실행파일 만들기
     - PyInstaller 모듈 설치
     ```shell
     > pip install pyinstaller
     > pyinstaller -w -F pythonfile.py
     ```
     - -w는 윈도우창만 실행 콘솔창삭제, -F _internal 폴더 생성안되도록, oneFile로 만들어 준다
     - 실패, 재생성시는 build, dist폴더 삭제, pythonfile.spec 삭제 뒤 다시 명령어 실행
  
   - Jupyter Notebook 사용법(빅데이터 분석, 코딩테스트)
     - Ctrl + Shift + P (명령 팔레트)
     - 노트북 사용
     - ChatGPT API 사용 
      [참조 사이트](https://github.com/teddylee777/openai-api-kr)
     - 메모장 만들기 :  [메모장만들기 예시](https://www.youtube.com/watch?v=6jPXGgON6oU&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&index=5)
