#!/home/ianp/dev/vacap/venv/bin/python3

import socket
import os
from _thread import *

def accept_client(connection, address):
    cl_str = ''
    for i in address_list:
        if(i != address):
            cl_str += str(i[0]) + ':' + str(i[1]) + '\n'
    connection.send(str.encode(cl_str))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


HOST = '127.0.0.1'
PORT = 2004

client_list = []
address_list = []

ServerSideSocket = socket.socket()
ServerSideSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


try:
    ServerSideSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(5)

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    client_list.append(Client)
    address_list.append(address)
    start_new_thread(accept_client, (Client, address))

ServerSideSocket.close()