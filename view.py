import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, \
    QHBoxLayout, QDesktopWidget


class LinkWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        self.setWindowTitle("link_to_world")
        self.resize(500, 500)  #窗口大小
        self.move(700, 300)  #窗口位置
        self.show() #窗口显示
        view1=QVBoxLayout(self)
        frm1=QFormLayout(self)
        lable1=QLabel("UserName:",self)
        edit1=QLineEdit(self)
        frm1.addRow(lable1,edit1)
        lable2=QLabel("Password:",self)
        edit2=QLineEdit(self)
        frm1.addRow(lable2, edit2)
        view1.addLayout(frm1)
        edit2.setEchoMode(QLineEdit.Password)
        btn1=QPushButton("Login",self)
        frm1.addRow(btn1)
        btn1.clicked.connect(self.btn1_click)
    def btn1_click(self):
        res=Chat()
        global list1
        list1.append(res)
class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        self.setWindowTitle("Chat_as_you_want")
        self.setGeometry(500, 200, 900, 600)  #绝对位置
        # self.resize(900, 600)  #窗口大小
        # self.move(500, 200)  #窗口位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        h1=QHBoxLayout(self)
        frm1 = QFormLayout(self)
        edit1=QLineEdit(self)
        edit1.setFocusPolicy(QtCore.Qt.NoFocus)
        edit1.setFixedHeight(400)
        edit1.setFixedWidth(300)
        edit2=QLineEdit(self)
        edit2.setFocusPolicy(QtCore.Qt.NoFocus)  #设置不可编辑
        edit2.setFixedHeight(400)
        edit2.setFixedWidth(600)
        frm1.addRow(edit1,edit2)
        label1=QLabel('pic',self)
        edit3=QLineEdit(self)
        # edit3.setFocusPolicy(QtCore.Qt.NoFocus)
        edit3.setFixedHeight(200)
        edit3.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        # edit3.setFixedWidth(600)
        frm1.addRow(label1,edit3)
        frm1.setSpacing(0)  #无缝
        h1.addLayout(frm1)
        self.show() #窗口显示
if __name__ == '__main__':
    app=QApplication(sys.argv)
    list1 = []
    a=LinkWorld()
    sys.exit(app.exec_())