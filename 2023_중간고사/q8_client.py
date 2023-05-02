from socket import *

BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

for i in range(4):
    time = 2
    msg = input('Enter a message("send mboxId message" or "receive mobxId"): ')
    if msg  == 'quit':
        sock.send(msg.encode())
        break
    while True:
        # msg = input('Enter a message("send mboxId message" or "receive mobxId"): ')
        # if msg  == 'quit':
        #     sock.send(msg.encode())
        #     break
        sock.send(msg.encode())
        print('Packet({}): Waiting up to {} secs for message'.format(i, time))
        sock.settimeout(time)
        try:
            data= sock.recv(BUFF_SIZE)
        except timeout:
            time += 2
            if time > 8:
                break
        else:
            print('Response', data.decode())
            break

sock.close()