import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QWaitCondition, Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolTip, QWidget
from PyQt5.QtGui import QIcon



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('First Application')
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('my tooltip')
        self.initUI()
    
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText('Adınız: ')
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Soyadınız: ')
        self.lbl_surname.move(50,70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(100,30)
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(100,70)
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Kaydet')
        self.btn_save.move(100,110)
        self.btn_save.clicked.connect(self.clicked)
        
    def clicked(self):
        print('butona tıklandı name: '+ self.txt_name.text(), 'surname: '+ self.txt_surname.text())


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


    
   
   

   

window() 