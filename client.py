import socket

from PyQt5.QtCore import QThread

from client_config import *


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.nickname = ''

    def register(self, name, pwd):
        str1 = "R " + name + ' ' + pwd
        self.client.sendto(str1.encode(), ADDR)
        data, addr = self.client.recvfrom(2048)
        info = data.decode()
        if info == 'OK':
            return True

    def login(self, name, pwd):
        str1 = "L " + name + ' ' + pwd
        self.client.sendto(str1.encode(), ADDR)
        data, addr = self.client.recvfrom(2048)
        info = data.decode().split(" ", 1)  # "OK friend friend   "
        if info[0] == 'OK':
            self.nickname = name
            return True, info[1]

    def send_msg(self, other, msg):
        str1 = "C " + self.nickname + " " + other + " " + msg
        self.client.sendto(str1.encode(), ADDR)

    def recv_msg(self):
        data, addr = self.client.recvfrom(2048)
        text = data.decode()
        return text


def recv_msg_thread():
    thread1 = Thread(target=deal_recv_msg)
    thread1.setDaemon(True)
    thread1.start()


code = 0


def deal_recv_msg():  # 无法实现
    global code
    code = code + 1
    if code == 1:
        result = s.recv_msg()
        if result:
            # result为朋友信息
            create_chat_window(result[1], s, list1)
            a.close()
        else:
            QMessageBox.information(a,  # 使用infomation信息框
                                    "Error",
                                    "登录失败",
                                    QMessageBox.Yes)
        print("over")
    result = s.recv_msg()
    print(result, 19, code)
    deal_recv_msg()
    # list1[0].show_msg(data)


class Mythread(QThread):
    pass

if __name__ == '__main__':
    list1 = []
    s = Client()
    app = QApplication(sys.argv)
    a = LinkWorld(s, list1)
    recv_msg_thread()
    sys.exit(app.exec_())
