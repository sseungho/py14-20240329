import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic # Qt Designer 에서 제작한 UI 불러오는 클래스

form_class = uic.loadUiType("ui/test.ui")[0]    #Qt Designer 에서 UI 호출

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 위에서 불러온 test.ui 연결
        self.setWindowTitle("It's Friday!")
        self.bttn01.clicked.connect(self.bttn01_click)
        # 버튼1이 클릭 >>> bttn01_click 메써드 호출
        self.bttn02.clicked.connect(self.bttn02_click)
        # 버튼1이 클릭 >>> bttn01_click 메써드 호출

    def bttn01_click(self):
        self.label1.setText('Hello World~~~')

    def bttn02_click(self):
        self.label1.setText('안녕~~~')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    sys.exit(app.exec_())

