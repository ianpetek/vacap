#!/home/ianp/dev/vacap/venv/bin/python3
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

SERVER_IP = '127.0.0.1'
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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.chat_refresh_timer = QTimer()
        self.chat_refresh_timer.setInterval(500)
        self.chat_refresh_timer.timeout.connect(self.refreshChat)
        self.chat_refresh_timer.start()

    def startListUpdateTimer(self):
        self.user_list_timer = QTimer()
        self.user_list_timer.setInterval(2000)
        self.user_list_timer.timeout.connect(self.updateUserList)
        self.user_list_timer.start()

    def LoginButtonClick(self):
        username = self.UsernameTextBox.toPlainText()
        server_ip = SERVER_IP
        server_port = SERVER_PORT

        if(self.connectToServer(server_ip, server_port, username)):
            self.stackedWidget.setCurrentIndex(1)
            self.updateUserList()
            start_new_thread(self.WaitForMsg, ())
            self.startListUpdateTimer()

    def sendMessage(self, msg, reciever_id, connection, recv_uname='client'):
        enc_message = msg.encode('utf-8')
        enc_msg_size = len(enc_message).to_bytes(2, 'big')
        enc_reciever_id = reciever_id.to_bytes(2, 'big')
        enc_name = recv_uname.encode('utf-8')
        enc_name_size = len(enc_name).to_bytes(1, 'big')
        connection.send(enc_msg_size + enc_reciever_id + enc_name_size)
        connection.send(enc_name)
        connection.send(enc_message)

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

    def RefreshButton(self):
        self.updateUserList()

    def userSelectButtonClicked(self, uname):
        self.curr_chat_label.setText(uname)
        self.curr_chat_user = uname
        self.textBrowser.setText(self.all_chats_by_uname[uname])

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

    def SendMessage(self):
        text = self.MessageBar.toPlainText()
        if(text == '' or self.curr_chat_user == ''):
            return
        self.sendMessage(text, 1000, self.clientSocket, self.curr_chat_user)
        self.all_chats_by_uname[self.curr_chat_user] += 'You: ' + text + '\n'
        self.refreshChat()
        self.MessageBar.clear()

    def WaitForMsg(self):
        while True:
            msg = self.recv_message(self.clientSocket)
            if(msg[1] == 1000):
                self.all_chats_by_uname[msg[2]
                                        ] += msg[2] + ': ' + msg[0] + '\n'
            elif(msg[1] == 9000):
                self.all_users = json.loads(msg[0])

    def refreshChat(self):
        if(not self.curr_chat_user == ''):
            self.textBrowser.setText(
                self.all_chats_by_uname[self.curr_chat_user])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
