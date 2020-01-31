import socket
from client_config import *


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



    def register(self, name, pwd):
        str1 = "R " + name + ' ' + pwd
        self.client.sendto(str1.encode(), ADDR)
        data, addr = self.client.recvfrom(2048)
        info = data.decode()
        if info == 'OK':
            return True
    def login(self,name,pwd):
        str1 = "L " + name + ' ' + pwd
        self.client.sendto(str1.encode(), ADDR)
        data, addr = self.client.recvfrom(2048)
        info = data.decode()
        if info == 'OK':
            return True

