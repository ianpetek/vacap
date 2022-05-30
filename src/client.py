#!/home/ianp/dev/vacap/venv/bin/python3

import socket
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
  
def sendMessage(msg, reciever_id, connection):
  enc_message = msg.encode('utf-8')
  enc_msg_size = len(enc_message).to_bytes(3, 'big')
  enc_reciever_id = reciever_id.to_bytes(2,'big')
  connection.send(enc_msg_size + enc_reciever_id)
  connection.send(enc_message)

def recv_message(connection):
  header = connection.recv(5)
  msg_size = int.from_bytes(header[:3], 'big')
  recv_id = int.from_bytes(header[3:], 'big')
  message_text = connection.recv(msg_size).decode('utf-8')
  print(message_text)

recv_message(ClientMultiSocket)
while True:
    Input = input('Hey there: ')
    sendMessage(Input, 0, ClientMultiSocket)
    header = ClientMultiSocket.recv(5)
    msg_size = int.from_bytes(header[:3], 'big')
    recv_id = int.from_bytes(header[3:], 'big')
    message_text = ClientMultiSocket.recv(msg_size)
    print(message_text.decode('utf-8'))