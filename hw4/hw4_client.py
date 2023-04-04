# TCPcalculator 클라이언트

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4444))

while True:
     msg = input('Enter formula: ')
     if msg == 'q':
          break
     s.send(msg.encode())

     print('Received message:', s.recv(1024).decode())

s.close()
