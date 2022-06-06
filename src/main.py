#!/home/ianp/dev/vacap/venv/bin/python3
import sys
import socket
import json

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
)

from main_window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def LoginButtonClick(self):
        username = self.UsernameTextBox.toPlainText()
        server_ip = self.ServerIpTextBox.toPlainText()
        server_port = int(self.PortTextBox.toPlainText())

        if(self.connectToServer(server_ip, server_port, username)):
            self.stackedWidget.setCurrentIndex(1)

        self.updateUserList()

    def sendMessage(self, msg, reciever_id, connection):
        enc_message = msg.encode('utf-8')
        enc_msg_size = len(enc_message).to_bytes(3, 'big')
        enc_reciever_id = reciever_id.to_bytes(2, 'big')
        connection.send(enc_msg_size + enc_reciever_id)
        connection.send(enc_message)

    def recv_message(self, connection):
        header = connection.recv(5)
        msg_size = int.from_bytes(header[:3], 'big')
        recv_id = int.from_bytes(header[3:], 'big')
        message_text = connection.recv(msg_size).decode('utf-8')
        return (message_text, recv_id)

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
        print('clicked ' + uname)

    def updateUserList(self):
        self.sendMessage('', 9888, self.clientSocket)
        recv_msg = self.recv_message(self.clientSocket)
        self.all_users = json.loads(recv_msg[0])

        for i in reversed(range(self.ChatSelectLayout.count())):
            widget = self.ChatSelectLayout.takeAt(i).widget()
            if(widget is not None):
                widget.setParent(None)

        for uname, addr in self.all_users.items():
            self.btn = QPushButton()
            self.btn.setText(uname)
            self.btn.clicked.connect(
                lambda ch, text=uname: self.userSelectButtonClicked(text))
            self.ChatSelectLayout.addWidget(self.btn)
        self.ChatSelectLayout.addStretch()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
