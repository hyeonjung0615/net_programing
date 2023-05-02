import socket
ip = '220.69.189.125'

a, b, c= (socket.gethostbyaddr(ip))
print(a)

port = socket.getservbyport(443)
print(port)

print(port + '://' + a)


print(socket.inet_aton(ip))