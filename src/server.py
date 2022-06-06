#!/home/ianp/dev/vacap/venv/bin/python3

import socket
import os
from _thread import *
import json


def sendMessage(msg, reciever_id, connection):
    enc_message = msg.encode('utf-8')
    enc_msg_size = len(enc_message).to_bytes(3, 'big')
    enc_reciever_id = reciever_id.to_bytes(2, 'big')
    connection.send(enc_msg_size + enc_reciever_id)
    connection.send(enc_message)


def accept_client(connection, address):
    header = connection.recv(5)
    msg_size = int.from_bytes(header[:3], 'big')
    name = connection.recv(msg_size).decode('utf-8')
    addr_name_lookup[address] = name
    name_addr_lookup[name] = address

    all_users_dump = json.dumps(name_addr_lookup)   
    sendMessage(all_users_dump, 0, connection)

    while True:
        header = connection.recv(5)
        if(header):
            msg_size = int.from_bytes(header[:3], 'big')
            recv_id = int.from_bytes(header[3:], 'big')
            message_text = connection.recv(msg_size)
            if(recv_id == 9888):
              all_users_dump = json.dumps(name_addr_lookup) 
              sendMessage(all_users_dump, 9888, connection)
            else:
              sendMessage(f"got your message of len {msg_size}", 0, connection)
        else:
            address_list.remove(address)
            client_list.remove(connection)
            name_addr_lookup.pop(name)
            addr_name_lookup.pop(address)
            break
    connection.close()


HOST = '127.0.0.1'
PORT = 2004

client_list = []
address_list = []
addr_name_lookup = {}
name_addr_lookup = {}

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