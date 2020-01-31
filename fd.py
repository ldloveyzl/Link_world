import socket
from multiprocessing import Process

from fd_config import *
from deal_sql import *
db=Database()
class Fd:
    def __init__(self):
        self.fd=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.bind_id(ADDR)
    # def deal_login(user,pwd):
    #


    def bind_id(self,addr):
        self.fd.bind(addr)
        self.fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def deal_req(self):
        data,addr=self.fd.recvfrom(2048)
        datas=data.decode().split(" ")
        req=datas[0]
        # 聊天 C name name1 msg
        # 登录 L name pwd
        # 注册 R name pwd
        if req=="R":
            self.register(datas[1],datas[2],addr)

    def register(self, name, pwd,addr):
        if db.register(name,pwd):
            self.fd.sendto("OK".encode(),addr)
        else:
            self.fd.sendto("NO".encode(), addr)
if __name__ == '__main__':
    f=Fd()
    f.deal_req()



