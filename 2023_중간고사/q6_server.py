from socket import *
import random
BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    msg = data.decode()
    print(msg)

    if msg != 'ping':
        continue

    else:
        if random.randint(1, 10) <=4:
            print('packet from {} lost!'.format(addr))
            continue
        sock.sendto(b'pong')
