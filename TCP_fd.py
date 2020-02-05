from socket import *
from client_config import *
TCP_client=socket()
TCP_client.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
TCP_client.bind(ADDR)
TCP_client.listen(3)
while True:
    confd,addr=TCP_client.accept()
    while True:
        data=TCP_client.recv(1024)
        data1=data.decode().split(" ")
        if data1[0]=="A":   #A name add_object

