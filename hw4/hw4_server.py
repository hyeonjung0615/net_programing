# TCPcalculator 서버

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(4)
print('waiting...')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)

        if not data:
            break
        try:
            data = data.decode()
            data = data.split() # 공백으로 스플릿

            if data[1] == '+':
                add = int(data[0]) + int(data[2])
                client.send(str(add).encode())

            elif data[1] == '-':
                sub = int(data[0]) - int(data[2])
                client.send(str(sub).encode())

            elif data[1] == '*':
                mul = int(data[0]) * int(data[2])
                client.send(str(mul).encode())

            elif data[1] == '/':
                div = int(data[0]) / int(data[2])
                div = "{:.1f}".format(div) # 소수점 첫째자리
                client.send(str(div).encode())

        except:
            client.send(b'Try again! Separate By Space!')
            
    client.close()

