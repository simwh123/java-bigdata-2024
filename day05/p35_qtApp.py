# file : p35_qtApp.py
# desc : PyQt5 앱 만들기
'''
PyQt5 -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QApplication 만들앱 전체 관리 클래스, Qwidget 메뉴가 없는 윈도우앱, QMainWindow 메뉴가 있는 윈도우앱
from PyQt5.QtWidgets import *

class qtApp(QWidget):   # Qwidget이 가지고 있는 속성, 변수, 함수를 다 사용가능 (상속)
    def __init__(self) -> None: 
        super().__init__()  # 생성자, 부모클래스의 생성자 함수도 실행되어야
        self.initUI();

    def initUI(self):
        self.setGeometry(700,300,800,400)   # 바탕화면 정해진 위치에 넓이와 높이로 그릴 설정
        self.setWindowTitle('첫번째 윈도우앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.show() # 윈도우창을 그림
    
    def paintEvent(self, event) -> None:
        paint = QPainter()  # 윈도우창 위에 그림그리는 객체
        paint.begin(self)   # 그림을 그리기 시작
        paint.setPen(QColor(10,10,10))  # RGB 색상 설정
        paint.setFont(QFont('Bauhaus 93',40)) # 폰트와 폰트 크기 설정
        paint.drawText(260,400//2,'Hello PyQt!')    # x,y축을 정해서 텍스트와 위치 설정
        paint.end()     # 반드시 닫아야 함

app = QApplication(sys.argv)    # 
inst = qtApp()  # 객체 생성
app.exec_() # 실행
