# from socket import *
import sys
import struct
import socket


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))

    msg = input("Start get message(Hello): ")
    
    s.send(msg.encode())
    msg = s.recv(1024)
    print(msg)
    Sender,Receiver,Lumi,Humi,Tmep,Air,Seq = struct.unpack(">HHBBBBI", msg[:12])
    print(Sender,Receiver,Lumi,Humi,Tmep,Air,Seq)

    print("Sender:{}, Receiver:{}, Lumi:{}, Humi:{}, Air:{}, Lumi:{}, Seq:{}".format(Sender,Receiver,Lumi,Humi,Tmep,Air,Seq))

    s.close()
