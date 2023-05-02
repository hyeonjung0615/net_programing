from socket import *

port = 2500
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

for i in range(4): # 4번 전송
    time = 1 # 1초
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    while True:
        sock.send(msg.encode())
        print('Packet({}): Waiting up to {} secs for ACK'. format(i, time))
        sock.settimeout(time)
        try:
            data = sock.recv(BUFFSIZE)
        except timeout:
            time += 1
            if time > 3:
                break
        else:
            print('Server says: ', data.decode())
            break

    # sock.close()    