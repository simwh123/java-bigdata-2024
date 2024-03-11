import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class winApp(QMainWindow): 
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()
        self.opened = False
        self.opened_file_path=''

    def initUI(self):
        uic.loadUi('C:/Source/java-bigdata-2024/day10/pynewMemo.ui',self)   
        self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowTitle('메모장')
        

        self.show()

    def initSignal(self):   # 메뉴/툴바 액션에 대한 시그널처리함수 선언
        self.action_newfile.triggered.connect(self.actionnewClicked)
        self.action_save.triggered.connect(self.actionsaveClicked)
        self.action_close.triggered.connect(self.actioncloseClicked)
        self.action_about.triggered.connect(self.actionaboutClicked)
        self.action_newsave.triggered.connect(self.actionnewsaveClicked)
    
    def save_file(self,fname):
        
        data = self.memo.toPlainText()

        with open(fname,'w', encoding='utf8')as f:
            f.write(data)
        self.opened = True
        self.opened_file_path =fname

    def open_file(self,fname):
        with open(fname[0], encoding='utf8') as f:
            data = f.read()
        self.memo.setPlainText(data)

        self.opened = True
        self.opened_file_path =fname

    def actionnewClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        with open(fname[0], encoding='utf8') as f:
            data = f.read()
        self.memo.setPlainText(data)
        print(fname[0])

    
    def actionsaveClicked(self):
        
        if self.opened:
            self.save_file(self.opened_file_path)
            
        else:
            fname = QFileDialog.getSaveFileName(self)
            if fname[0]:
                self.save_file(fname[0])



    def actioncloseClicked(self):
        re = QMessageBox.question(self,'종료','저장후 종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            fname = QFileDialog.getSaveFileName(self,'텍스트저장','','text file(*.txt)')
            if fname[0]:
                data = self.memo.toPlainText()

                with open(fname[0],'w', encoding='utf8')as f:
                    f.write(data)
            exit(0)  

    def actionaboutClicked(self):
        QMessageBox.about(self,'hi','hi')
    
    def actionnewsaveClicked(self):
            fname = QFileDialog.getSaveFileName(self)
            if fname[0]:
                    self.save_file(fname[0])



    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else : 
            QCloseEvent.ignore()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = winApp()
    sys.exit(app.exec_())