import socket
import random

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')


while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if random.randint(1, 10) <= 4: # 40% 데이터 손실
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(msg.decode(), addr))
    # print('Received: ', msg.decode())

    sock.sendto( b'ACK. Echo msg: '+ msg, addr)
