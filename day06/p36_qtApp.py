# file : p36_qtApp.py
# desc : PyQt5 앱 만들기(이어서)
'''
PyQt5 -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력을 다 사용할 수 있음)
from PyQt5.QtWidgets import *

class qtApp(QWidget):   
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self):
        label = QLabel() # 라벨위젯(qt, PyQt) == 라벨컨트롤(MFC, C#, Java Fx, Android)
        
        self.setGeometry(700,300,800,400)   
        self.setWindowTitle('두번째 qt앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.text = 'What a wonderful world. . .'
        label.setText(self.text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(('color: red;'
                             'background-color: black;')) # 라벨의 색상스타일 설정 html css와 완전 동일
        
        font = label.font()
        font.setFamily('Bauhaus 93')
        font.setPointSize(40)
        

        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.show() 
    
    def paintEvent(self, event) -> None:
        paint = QPainter()  
        paint.begin(self)   
        paint.setPen(QColor(100,100,100))  
        paint.setFont(QFont('Bauhaus 93',40)) 
        paint.drawText(260,400//2,'Hello PyQt!')    
        paint.end()     

app = QApplication(sys.argv)     
inst = qtApp()  
app.exec_() 
