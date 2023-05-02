from socket import *

BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

mbox = {}

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    msg = data.decode()
    # msg = msg.split()
    # print(msg) # 메시지 스플릿 확인용
    
    if msg == 'quit':
        break

    msg = msg.split()
    # print(msg) # 메시지 스플릿 확인용

    # 메시지 유형에 따라 처리
    if msg[0] == 'send':
        mbox_id = msg[1]
        message = ' '.join(msg[2:])

        if mbox_id not in mbox:
            mbox[mbox_id] = []

        mbox[mbox_id].append(message)
        sock.sendto('OK'.encode(), addr)
        # print(mbox) # 확인용

    elif msg[0] == 'receive':
        mbox_id = msg[1]
        if (mbox_id not in mbox) or (not mbox[mbox_id]):
            sock.sendto(b'No messages', addr)
        else:
            sendM = mbox[mbox_id].pop(0) # 맨 앞에꺼 가져와서 SD에 저장
            print(sendM)
            sock.sendto(sendM.encode(), addr)

sock.close()