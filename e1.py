import socket
from multiprocessing import Process

class Fd:
    def __init__(self):
        self.fd()
    def deal_login(user,pwd):

    def fd(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind(('0.0.0.0',7877))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.deal_req(s)

    def deal_req(self, s):
        data,addr=s.recvfrom(2048)  #Login user pwd   Chat msg user
        data=


