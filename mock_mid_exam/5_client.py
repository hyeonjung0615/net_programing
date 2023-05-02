from socket import *

BUFF_SIZE = 1024
port = 6565

# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('localhost', port))


while True:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', port))

    msg = input('Enter a message("send mboxId message" or "receive mobxId"): ')
    if msg  == 'quit':
        sock.send(msg.encode())
        break

    sock.send(msg.encode())
    data = sock.recv(BUFF_SIZE)
    print(data.decode())

sock.close()





### chat GPT 
# from socket import *

# BUFF_SIZE = 1024
# port = 6565

# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('localhost', port))

# while True:
#     msg = input('Enter a message("send mboxId message" or "receive mobxId"): ')
#     if msg == 'quit':
#         sock.send(msg.encode())
#         break

#     sock.send(msg.encode())
#     data = sock.recv(BUFF_SIZE)
#     print(data.decode())

# sock.close()
