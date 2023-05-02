from socket import *
import threading

port = 2500
BUFSIZE = 1024

def handler(sock):
    while True:
        data = sock.recv(BUFSIZE)
        print(data.decode())

    sock.close() 

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

my_id = input('ID를 입력하세요:')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock,))
# th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    sock.send(msg.encode())

