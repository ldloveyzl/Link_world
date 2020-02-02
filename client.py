import socket
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
            return info[1]

    def send_msg(self, other, msg):
        str1 = "C " + self.nickname + " " + other + " " + msg
        self.client.sendto(str1.encode(), ADDR)

    def recv_msg(self):
        data, addr = self.client.recvfrom(2048)
        text=data.decode()

