from socket import *

BUFF_SIZE = 1024
port = 6565

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

mbox= {}

while True:
    c, addr = sock.accept()

    data = c.recv(BUFF_SIZE)
    msg = data.decode()

    if msg == 'quit':
        break
    
    msg = msg.split()

    if msg[0] == 'send':
        mbox_id = msg[1]
        message = ' '.join(msg[2:])

        if mbox_id not in mbox:
            mbox[mbox_id] = []

        mbox[mbox_id].append(message)
        c.send('OK'.encode())

    elif msg[0] == 'receive':
        mbox_id = msg[1]
        if (mbox_id not in mbox) or (not mbox[mbox_id]):
            c.send(b'No messages')
        else:
            sendM = mbox[mbox_id].pop(0) # 맨 앞에꺼 가져와서 SD에 저장
            print(sendM)
            c.send(sendM.encode())

    c.close()

sock.close()




### chat GPT
# from socket import *

# BUFF_SIZE = 1024
# port = 6565

# sock = socket(AF_INET, SOCK_STREAM)
# sock.bind(('', port))
# sock.listen(1)

# mbox = {}

# while True:
#     conn, addr = sock.accept()
#     print('Connected by', addr)

#     while True:
#         data = conn.recv(BUFF_SIZE)
#         msg = data.decode()
#         # msg = msg.split()
#         # print(msg) # 메시지 스플릿 확인용
        
#         if msg == 'quit':
#             break

#         msg = msg.split()
#         # print(msg) # 메시지 스플릿 확인용

#         # 메시지 유형에 따라 처리
#         if msg[0] == 'send':
#             mbox_id = msg[1]
#             message = ' '.join(msg[2:])

#             if mbox_id not in mbox:
#                 mbox[mbox_id] = []

#             mbox[mbox_id].append(message)
#             conn.sendall('OK'.encode())
#             # print(mbox) # 확인용

#         elif msg[0] == 'receive':
#             mbox_id = msg[1]
#             if (mbox_id not in mbox) or (not mbox[mbox_id]):
#                 conn.sendall(b'No messages')
#             else:
#                 sendM = mbox[mbox_id].pop(0) # 맨 앞에꺼 가져와서 SD에 저장
#                 print(sendM)
#                 conn.sendall(sendM.encode())

#     conn.close() # 메시지 처리 후 연결 끊음

# sock.close()
