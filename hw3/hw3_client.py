import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

sock.send(b'hyeonjung Noh')

msg_SN = sock.recv(1024)
msg_SN = int.from_bytes(msg_SN, 'big')
print(msg_SN)

sock.close()
