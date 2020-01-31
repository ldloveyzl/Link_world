import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from client import *

s = Client()
class LinkWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setWindowTitle("link_to_world")
        self.resize(500, 500)  # 窗口大小
        self.move(700, 300)  # 窗口位置
        self.show()  # 窗口显示
        view1 = QVBoxLayout(self)
        frm1 = QFormLayout(self)

        lable1 = QLabel("UserName:", self)
        self.name = QLineEdit(self)
        frm1.addRow(lable1, self.name)

        lable2 = QLabel("Password:", self)
        self.pwd = QLineEdit(self)
        frm1.addRow(lable2, self.pwd)

        view1.addLayout(frm1)
        self.pwd.setEchoMode(QLineEdit.Password)
        btn1 = QPushButton("Resgister", self)
        btn2 = QPushButton("Login", self)
        frm1.addRow(btn1, btn2)
        btn1.clicked.connect(self.btn1_click)
        btn2.clicked.connect(self.btn2_click)

    def btn1_click(self):
        n = self.name.text()
        p = self.pwd.text()
        if not s.register(n,p):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "Sorry~",
                                    "注册失败",
                                    QMessageBox.Yes)


    def btn2_click(self):
        res = Chat()
        global list1
        list1.append(res)


class Chat(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.talk_to = ""

    def outSelect(self, Item=None):
        if not Item:
            self.talk_to = Item.text()

    def UI(self):
        self.setWindowTitle("Chat_as_you_want")
        self.setGeometry(500, 200, 900, 600)  # 绝对位置
        # self.resize(900, 600)  #窗口大小
        # self.move(500, 200)  #窗口位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        h1 = QHBoxLayout(self)
        frm1 = QFormLayout(self)

        widget1 = QTableWidget()
        widget1.setColumnCount(2)
        widget1.setRowCount(5)
        widget1.horizontalHeader().setVisible(False)
        # 设置QTableWidget列宽固定
        widget1.horizontalHeader().resizeSection(0, 117)
        widget1.horizontalHeader().resizeSection(1, 118)
        # tableWidget->verticalHeader()->setDefaultSectionSize(10); //设置行高
        widget1.verticalHeader().setDefaultSectionSize(35)
        widget1.itemClicked.connect(self.outSelect)  # 单击获取单元格中的内容

        edit2 = QLineEdit(self)
        edit2.setFocusPolicy(QtCore.Qt.NoFocus)  # 设置不可编辑
        edit2.setFixedHeight(400)
        edit2.setFixedWidth(600)

        frm1.addRow(widget1, edit2)

        label1 = QLabel('pic', self)
        edit3 = QLineEdit(self)
        # edit3.setFocusPolicy(QtCore.Qt.NoFocus)
        edit3.setFixedHeight(200)
        edit3.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # edit3.setFixedWidth(600)

        frm1.addRow(label1, edit3)
        frm1.setSpacing(0)  # 无缝

        h1.addLayout(frm1)
        self.show()  # 窗口显示



if __name__ == '__main__':
    app = QApplication(sys.argv)
    list1 = []
    a = LinkWorld()
    sys.exit(app.exec_())
