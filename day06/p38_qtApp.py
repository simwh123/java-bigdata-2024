# file : p38_qtApp.py
# desc : PyQt5, PyQt5Designer 같이사용하여 앱 만들기(이어서)
'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qtApp(QWidget):   
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self):   # ui파일을 로드해서 화면디자인  사용
        uic.loadUi('./day06/firstApp.ui',self)
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) # ui파일내 위젯은 자동완성X
       
        self.show() 

    def btnMsgClicked(self):
        self.label.setText('What a wonderful world. . .')
        QMessageBox.about(self,'Qt디자이너','클릭하였습니다!!!!')
        
    def closeEvent(self, QCloseEvent) -> None:  # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:   #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    #무시
 

app = QApplication(sys.argv)     
inst = qtApp()  
app.exec_() 
