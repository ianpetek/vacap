from importlib.abc import TraversableResources
import sys
import socket
import json
from _thread import *
import time

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
)
from PyQt5.QtCore import QTimer, QDateTime

from main_window_ui import Ui_MainWindow
from PyQt5 import uic

SERVER_IP = '174.138.11.137'
SERVER_PORT = 2004


''' pavle verzija
class Window(QMainWindow, Ui_MainWindow):
    curr_chat_user = ''
    all_chats_by_uname = {}

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('C:\\lokacija\\filea\\main_window.ui', self)
'''


class Window(QMainWindow, Ui_MainWindow):
    curr_chat_user = ''
    all_chats_by_uname = {}

    # Init function that setups the UI and starts the refreshChat interval timer
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.chat_refresh_timer = QTimer()
        self.chat_refresh_timer.setInterval(500)
        self.chat_refresh_timer.timeout.connect(self.refreshChat)
        self.chat_refresh_timer.start()

    # Function that starts an interval timer that updates online user list
    def startListUpdateTimer(self):
        self.user_list_timer = QTimer()
        self.user_list_timer.setInterval(2000)
        self.user_list_timer.timeout.connect(self.updateUserList)
        self.user_list_timer.start()

    # Function that is called after the login button is pressed
    def LoginButtonClick(self):
        username = self.UsernameTextBox.toPlainText()
        server_ip = SERVER_IP
        server_port = SERVER_PORT

        if(self.connectToServer(server_ip, server_port, username)):
            self.stackedWidget.setCurrentIndex(1)
            self.updateUserList()
            start_new_thread(self.WaitForMsg, ())
            self.startListUpdateTimer()

    # Utility function for sending messages to the server.
    # msg - message of max len of 2^16 characters
    # reciever_id - type of mesage (9000 get users request, 1000 normal message send)
    # connection - socket connection to server
    # recv_uname - message reciever username
    def sendMessage(self, msg, type_id, connection, recv_uname='client'):
        enc_message = msg.encode('utf-8')
        enc_msg_size = len(enc_message).to_bytes(2, 'big')
        enc_type_id = type_id.to_bytes(2, 'big')
        enc_name = recv_uname.encode('utf-8')
        enc_name_size = len(enc_name).to_bytes(1, 'big')
        connection.send(enc_msg_size + enc_type_id + enc_name_size)
        connection.send(enc_name)
        connection.send(enc_message)

    # Utility function for recieving messages
    # return - a tuple of message_text, type_id, recv_uname
    def recv_message(self, connection):
        header = connection.recv(5)
        if(not header):
            return False
        msg_size = int.from_bytes(header[:2], 'big')
        recv_id = int.from_bytes(header[2:4], 'big')
        name_size = int.from_bytes(header[4:], 'big')
        recv_uname = connection.recv(name_size).decode('utf-8')
        message_text = connection.recv(msg_size).decode('utf-8')
        return (message_text, recv_id, recv_uname)

    # Function for initial connecting to the server
    def connectToServer(self, HOST, PORT, username):
        self.clientSocket = socket.socket()
        self.HOST = HOST
        self.PORT = PORT
        self.USERNAME = username

        try:
            self.clientSocket.connect((self.HOST, self.PORT))
        except socket.error as e:
            print(str(e))
            return False

        # Send username
        self.sendMessage(username, 0, self.clientSocket)
        recv_msg = self.recv_message(self.clientSocket)
        self.all_users = json.loads(recv_msg[0])
        return True

    # A function that is called when one of the online user button is clicked
    def userSelectButtonClicked(self, uname):
        self.curr_chat_label.setText(uname)
        self.curr_chat_user = uname
        self.textBrowser.setText(self.all_chats_by_uname[uname])

    # Fetches the list of all online user and updates the ui
    def updateUserList(self):
        self.sendMessage('', 9000, self.clientSocket)
        time.sleep(0.2)
        for i in reversed(range(self.ChatSelectLayout.count())):
            widget = self.ChatSelectLayout.takeAt(i).widget()
            if(widget is not None):
                widget.setParent(None)

        for uname in self.all_users:
            if(uname == self.USERNAME):
                continue
            if(uname not in self.all_chats_by_uname):
                self.all_chats_by_uname[uname] = ''

            self.btn = QPushButton()
            self.btn.setText(uname)
            self.btn.clicked.connect(
                lambda ch, text=uname: self.userSelectButtonClicked(text))
            self.ChatSelectLayout.addWidget(self.btn)
        self.ChatSelectLayout.addStretch()

    def LabelAppear(self):
        self.label_4.setText(
            'Kako koristiti ovaj program?\nNapišite svoj username po želji.\nKada stisnete login pojavit će se lista sa svim dostupnim korisnicima\ns kojima možete komunicirati.')
        self.pushButton.setHidden(True)
        self.label_5.setHidden(True)

    def LabelHide(self):
        self.label_4.setText('')
        self.pushButton.setHidden(False)
        self.label_5.setHidden(False)

    # Function that is called after the send message button is pressed
    def SendMessage(self):
        text = self.MessageBar.toPlainText()
        if(text == '' or self.curr_chat_user == ''):
            return
        self.sendMessage(text, 1000, self.clientSocket, self.curr_chat_user)
        self.all_chats_by_uname[self.curr_chat_user] += 'You: ' + text + '\n'
        self.refreshChat()
        self.MessageBar.clear()

    # Function called in a seperate thread that waits for incoming messages
    def WaitForMsg(self):
        while True:
            msg = self.recv_message(self.clientSocket)
            if(msg[1] == 1000):
                self.all_chats_by_uname[msg[2]
                                        ] += msg[2] + ': ' + msg[0] + '\n'
            elif(msg[1] == 9000):
                self.all_users = json.loads(msg[0])

    # Function that refreshes the chat area with new messages
    def refreshChat(self):
        if(not self.curr_chat_user == ''):
            self.textBrowser.setText(
                self.all_chats_by_uname[self.curr_chat_user])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
