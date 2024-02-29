# file : p45_threadApp.py
# desc : PyQt5 스레드 학습용(스레드 사용)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackGroundWorker(QThread): # PyQt용 스레드
    initUiSignal = pyqtSignal(int)  # 스레드로 진행할때 UI에서 초기에 처리할 초기화부분 시그널 전달
    setPgbSignal = pyqtSignal(int)  # 스레드 진행시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str)  # 스레드 진행시 화면에 출력될 문자열을 UI쪽으로 전달
    
    def __init__(self, parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        maxVal = 100_000
        self.initUiSignal.emit(maxVal)   # 나는 값을 보내니 UI쪽(qtApp)에서 받아서 처리해줘
        
        for i in range(maxVal):
            print(f'쓰레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'쓰레드 진행 >> {i}')
            #self.parent.pgbTask.setValue(i) # UI스레드의 권한을 백그라운드스레드에 주지않는다.
            #self.parent.txbLog.append(f'쓰레드 진행 >> {i}')    # 사용불가


class qtApp(QWidget):   
    def __init__(self) -> None: 
        super().__init__()  
        self.initUI()

    def initUI(self):   # ui파일을 로드해서 화면디자인  사용
        uic.loadUi('./day07/testThread.ui',self)
        self.setWindowTitle('쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일내 위젯은 자동완성X
       
        self.show() 

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackGroundWorker(self) # qtApp 부모클래스라고
        th.start() # 스레드내 run()함수실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)

        self.btnStart.setEnabled(True)
    
    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int)  # pyqtSignal에서 넘어온 값을 처리해주는 부분이라고 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0,maxVal-1)
        
        
    def closeEvent(self, QCloseEvent) -> None:  # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes:   #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    #무시
 

app = QApplication(sys.argv)     
inst = qtApp()  
app.exec_() 