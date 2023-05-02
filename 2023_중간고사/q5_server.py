from socket import *
import sys
import random
import struct 
import binascii


sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)
print('waiting...')

while True:
    c, addr = sock.accept()
    msg = c.recv(1024)
    msg = msg.decode()

    if msg == '1':
        Temp = random.randint(1, 50) # Temperature
        print(Temp)
        sm = struct.pack('!iii', Temp, 0 , 0)
        print(sm)
        c.send(sm)

    elif msg == '2':
        Humid = random.randint(1, 100) # Humidity
        print(Humid)
        sm = struct.pack('!iii', 0, Humid , 0)
        print(sm)
        c.send(sm)

    elif msg == '3':
        Illum = random.randint(1, 150) # Illuminance
        print(Humid)
        sm = struct.pack('!iii', 0, 0 , Illum)
        print(sm)
        c.send(sm)
        
