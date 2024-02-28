# file : p39_naverNews.py
# desc : PyQt5, PyQt5Designer 같이사용하여 네이버뉴스 검색 만들기

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import webbrowser # 기본 웹브라우저 모듈
from naverSearch import NaverSearch
import time


class qtApp(QWidget):   
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self):   # ui파일을 로드해서 화면디자인  사용
        uic.loadUi('./day06/naverNews.ui',self)
        self.setWindowIcon(QIcon('./images/news.png'))
        # 버튼 시그널처리
        self.btnSearch.clicked.connect(self.btnSearchClicked) # ui파일내 위젯은 자동완성X
        self.txtSearchWord.returnPressed.connect(self.btnSearchClicked) # 검색버튼 시그널함수를 연결!
        self.tblSearchResult.itemSelectionChanged.connect(self.tblResultSelected)

        
        self.show() 

    def tblResultSelected(self):    # 테이블 클릭시 처리
        selectRow = self.tblSearchResult.currentRow()  # 현재 선택된 행의 인덱스
        url = self.tblSearchResult.item(selectRow,1).text()
        # QMessageBox.about(self,'popup',url)
        webbrowser.open(url)

    def btnSearchClicked(self): # 검색 버튼 클릭시 처리
        searchWord = self.txtSearchWord.text().strip()
       

        if(len(searchWord)) == 0:   # Validation Check(입력)
            QMessageBox.about(self,'네이버 검색','검색어를 입력하세요.')
            return # 함수탈출
        
        #검색시작
        api = NaverSearch() # api 객체생성
        jsonSearch = api.getSerachResult(searchWord)
        #print(jsonSearch)
        self.makeListView(jsonSearch)

    def makeListView(self, data):
        result = data['items']  # 네이버 검색결과의 키 items의 값들만 활용
        # tblSearchResult 리스트뷰 작업시작
        self.tblSearchResult.setColumnCount(3)
        self.tblSearchResult.setRowCount(len(result))   # 10개면 10개
        self.tblSearchResult.setHorizontalHeaderLabels(['기사제목','뉴스링크','게시일자'])

        n = 0
        for post in result:
            self.tblSearchResult.setItem(n,0,QTableWidgetItem(post['title']))
            self.tblSearchResult.setItem(n,1,QTableWidgetItem(post['link']))
          
            tempDate = str(post['pubDate']).split(' ')  # 게시일을 년-월-일로 나타낸다
            year = tempDate[3]
            month = time.strptime(tempDate[2],'%b').tm_mon
            month = f'{month:02d}'
            day = tempDate[1]
            date = f'{year}-{month}-{day}'
           
            self.tblSearchResult.setItem(n,2,QTableWidgetItem(date))
            n += 1
        
        # 컬럼 길이 변경
        self.tblSearchResult.setColumnWidth(0,465)  
        self.tblSearchResult.setColumnWidth(1,200)
        self.tblSearchResult.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 컬럼 더블블릭 금지

        
    def closeEvent(self, QCloseEvent) -> None:  # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:   #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    #무시


app = QApplication(sys.argv)     
inst = qtApp()  
app.exec_() 