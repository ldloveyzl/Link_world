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
        elif req=='L':
            self.login(datas[1],datas[2],addr)
        elif req=="C":
            self.chat(datas[1],datas[2],datas[3])
        elif req=='H':
            self.has_msg(datas[1])

    def register(self, name, pwd,addr):
        if db.register(name,pwd):
            self.fd.sendto("OK".encode(),addr)
        else:
            self.fd.sendto("NO".encode(), addr)

    def login(self, name, pwd, addr):
        if db.login(name, pwd,addr):
            print(addr)
            friends=self.get_friends(name)
            msg="OK"+" "+friends
            self.fd.sendto(msg.encode(), addr)
        else:
            self.fd.sendto("NO".encode(), addr)

    def get_friends(self,name):
        return db.getfriends(name)

    def chat(self, name, friend, msg):
        friend_addr=db.get_friend_addr(friend)
        msg=name+":"+msg
        self.fd.sendto(msg.encode(),friend_addr)
        print(msg,"发给",friend_addr)
        db.save_msg(name,friend,msg)

    def has_msg(self, name):
        pass


if __name__ == '__main__':
    f=Fd()
    while True:
        f.deal_req()



