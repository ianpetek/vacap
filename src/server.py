#!/home/ianp/dev/vacap/venv/bin/python3

import socket
import os
from _thread import *
import json

## 9000 recv_id get user list
## 1000 recv_id messages

def sendMessage(msg, reciever_id, connection, recv_uname = 'server'):
      enc_message = msg.encode('utf-8')
      enc_msg_size = len(enc_message).to_bytes(2, 'big')
      enc_reciever_id = reciever_id.to_bytes(2, 'big')
      enc_name = recv_uname.encode('utf-8')
      enc_name_size = len(enc_name).to_bytes(1, 'big')
      connection.send(enc_msg_size + enc_reciever_id + enc_name_size)
      connection.send(enc_name)
      connection.send(enc_message)

def recv_message(connection):
      header = connection.recv(5)
      if(not header):
        return False
      msg_size = int.from_bytes(header[:2], 'big')
      recv_id = int.from_bytes(header[2:4], 'big')
      name_size = int.from_bytes(header[4:], 'big')
      recv_uname = connection.recv(name_size).decode('utf-8')
      message_text = connection.recv(msg_size).decode('utf-8')
      return ( message_text, recv_id, recv_uname)

def accept_client(connection, address):
    recv = recv_message(connection)
    name = recv[0]
    addr_name_lookup[address] = name
    name_addr_lookup[name] = address
    name_client_lookup[name] = connection

    all_users_dump = json.dumps(list(name_addr_lookup.keys()))   
    sendMessage(all_users_dump, 0, connection)

    while True:
        recv = recv_message(connection)
        if(recv):
            if(recv[1] == 9000):
              all_users_dump = json.dumps(list(name_addr_lookup.keys())) 
              sendMessage(all_users_dump, 9000, connection)
            elif(recv[1] == 1000):
              try:
                msg_reciever = name_client_lookup[recv[2]]
                sendMessage(recv[0], recv[1], msg_reciever, recv_uname = name)
              except:
                print("Couldnt send message")
            else:
              sendMessage(f"got your message of len", 0, connection)
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
name_client_lookup = {}

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