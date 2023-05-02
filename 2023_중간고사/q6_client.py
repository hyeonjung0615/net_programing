from socket import *

BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('ping start: ')
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFF_SIZE)
    print()