#!/home/ianp/dev/vacap/venv/bin/python3

import socket
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))#


res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'))
while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))