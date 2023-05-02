# from socket import *
import sys
import struct
import socket


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8888))

    msg = input("input number(1~3)")
    
    s.send(msg.encode())
    msg = s.recv(1024)
    print(msg)
    t, h, i = struct.unpack(">III", msg[:12])
    print(t,h,i)
    print("Temp:{}, Humid:{}, Lumi:{}".format(t,h,i))

    s.close()
