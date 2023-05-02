from socket import *

BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter a message("send mboxId message" or "receive mobxId"): ')
    if msg  == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
        break

    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFF_SIZE)
    print(data.decode())

sock.close()