from socket import *
import random
import struct

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(5)
print('waiting...')

while True:
    c, addr = sock.accept()
    msg = c.recv(1024)
    msg = msg.decode()

    if msg == 'Hello':
        Sender = random.randint(1, 50000)
        Receiver = random.randint(1, 50000)
        Lumi = random.randint(1, 100)
        Humi = random.randint(1, 100)
        Tmep = random.randint(1, 100)
        Air = random.randint(1, 100)
        Seq = random.randint(1, 100000)
        sum = struct.pack('!HHBBBBI',Sender,Receiver,Lumi,Humi,Tmep,Air,Seq)
        print(sum)
        c.send(sum)

