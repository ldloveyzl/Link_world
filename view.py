import time
from multiprocessing import Process
from threading import Thread

from PyQt5.QtCore import QCoreApplication, QTimer
import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from threading import Lock
from client import *
from multiprocessing import Queue
from add_guy import *
rec_msg = Queue()


def create_chat_window(result):
    res = Chat(result)
    list1.append(res)


def recv_msg_process():
    process1 = Process(target=recv_msg)
    process1.daemon=True
    process1.start()
    print("已启动")



def recv_msg():  # 无法实现
    while True:
        data = s.recv_msg()
        rec_msg.put(data)


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
        s.register(n, p)
        result = rec_msg.get()
        print(result,'print')
        if result=='OK':
            QMessageBox.information(self,  # 使用infomation信息框
                                    "Sorry~",
                                    "注册失败",
                                    QMessageBox.Yes)
        else:
            QMessageBox.information(self,  # 使用infomation信息框
                                    "Congratulate!",
                                    "注册成功",
                                    QMessageBox.Yes)

    def btn2_click(self):
        n = self.name.text()
        p = self.pwd.text()
        s.login(n, p)
        result=rec_msg.get()
        info = result.split(" ", 1)  # "OK friend friend   "
        if info[0] == 'OK':
            # result为朋友信息
            create_chat_window(info[1])
            s.nickname=n
            self.close()
        else:
            QMessageBox.information(self,  # 使用infomation信息框
                                    "Error",
                                    "登录失败",
                                    QMessageBox.Yes)


class Chat(QWidget):
    def __init__(self, result):
        super().__init__()
        self.friends = result
        self.msg_box = QTextEdit(self)
        self.msg = QLineEdit(self)
        self.UI()
        print(result)  # 删除
        self.talk_to = ""
        self.timer = QTimer(self)  # 呼叫 QTimer
        self.timer.timeout.connect(self.show_msg)  # 當時間到時會執行 run
        self.timer.start(1000)  # 啟動 Timer .. 每隔1000ms 會觸發 run
        self.total = 0  # 初始 total

    def show_msg(self):
        # s.has_msg()
        if rec_msg.empty():
            return
        data=rec_msg.get()
        text = self.msg_box.toPlainText()
        text += data + "\n"
        self.msg_box.setPlainText(text)

    def outSelect(self, Item=None):
        if Item:
            self.talk_to = Item.text()

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if self.msg.hasFocus() and key == Qt.Key_Return and self.talk_to:
            data = self.msg.text()
            other = self.talk_to
            s.send_msg(other, data)
            self.msg.clear()

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

        friend_info = self.friends.split(" ")
        l = len(friend_info)

        widget1 = QTableWidget()
        widget1.setColumnCount(2)
        widget1.setRowCount(l)
        widget1.horizontalHeader().setVisible(False)
        # 设置QTableWidget列宽固定
        widget1.horizontalHeader().resizeSection(0, 117)
        widget1.horizontalHeader().resizeSection(1, 118)
        # tableWidget->verticalHeader()->setDefaultSectionSize(10); //设置行高
        widget1.verticalHeader().setDefaultSectionSize(35)
        for i in range(l):
            widget1.setItem(i, 0, QTableWidgetItem(friend_info[i]))
        widget1.itemClicked.connect(self.outSelect)  # 单击获取单元格中的内容

        self.msg_box.setFocusPolicy(QtCore.Qt.NoFocus)  # 设置不可编辑
        self.msg_box.setFixedHeight(400)
        self.msg_box.setFixedWidth(600)

        frm1.addRow(widget1, self.msg_box)

        label1 = QLabel('pic', self)
        # edit3.setFocusPolicy(QtCore.Qt.NoFocus)

        self.msg.setFixedHeight(200)
        self.msg.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # edit3.setFixedWidth(600)

        frm1.addRow(label1, self.msg)
        frm1.setSpacing(0)  # 无缝

        h1.addLayout(frm1)
        self.show()  # 窗口显示
    def add_friend(self):




if __name__ == '__main__':
    # chat_started()
    s = Client()
    recv_msg_process()
    list1 = []
    app = QApplication(sys.argv)
    a = LinkWorld()
    sys.exit(app.exec_())
