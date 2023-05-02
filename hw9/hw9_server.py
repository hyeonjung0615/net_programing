from socket import *
import time
import threading

port = 2500
BUFSIZE = 1024

client_sockets = []

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(9)

print('server Started')


def handle_client(cli_S):
    while True:
        data = cli_S.recv(BUFSIZE)
        if not data:
            break

        print(time.asctime() + str(cli_S) + ':' + data.decode())

        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if cli_S in client_sockets:
                print(cli_S, 'exited')
                client_sockets.remove(cli_S)
                continue

        # 모든 클라이언트에게 전송
        for client in client_sockets:
            if client != cli_S:
                client.send(data)

    cli_S.close()            
    
while True:
    cli_S, addr = s.accept()

    # 새로운 클라이언트이면 목록에 추가
    if cli_S not in client_sockets:
        print('new client', cli_S)
        client_sockets.append(cli_S)

    th = threading.Thread(target=handle_client, args=(cli_S,))
    th.start()

s.close()
