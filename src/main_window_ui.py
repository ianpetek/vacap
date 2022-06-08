# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 635)
        MainWindow.setStyleSheet("background-color: rgb(37, 211, 102);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 851, 611))
        self.stackedWidget.setStyleSheet("background-color: rgb(37, 211, 102);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.UsernameTextBox = QtWidgets.QTextEdit(self.loginPage)
        self.UsernameTextBox.setGeometry(QtCore.QRect(280, 280, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UsernameTextBox.setFont(font)
        self.UsernameTextBox.setAutoFillBackground(False)
        self.UsernameTextBox.setObjectName("UsernameTextBox")
        self.label = QtWidgets.QLabel(self.loginPage)
        self.label.setGeometry(QtCore.QRect(430, 250, 71, 17))
        self.label.setObjectName("label")
        self.LoginButton = QtWidgets.QPushButton(self.loginPage)
        self.LoginButton.setGeometry(QtCore.QRect(390, 470, 141, 41))
        self.LoginButton.setStyleSheet("background-color: rgb(183, 248, 255);")
        self.LoginButton.setObjectName("LoginButton")
        self.pushButton = QtWidgets.QPushButton(self.loginPage)
        self.pushButton.setGeometry(QtCore.QRect(110, 530, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(183, 248, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.loginPage)
        self.label_4.setGeometry(QtCore.QRect(190, 30, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.loginPage)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 530, 131, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(183, 248, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.loginPage)
        self.label_5.setGeometry(QtCore.QRect(290, 50, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_2.raise_()
        self.UsernameTextBox.raise_()
        self.label.raise_()
        self.LoginButton.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.loginPage)
        self.chatPage = QtWidgets.QWidget()
        self.chatPage.setObjectName("chatPage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.chatPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 161, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ChatSelectLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ChatSelectLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ChatSelectLayout.setContentsMargins(0, 0, 0, 0)
        self.ChatSelectLayout.setObjectName("ChatSelectLayout")
        self.MessageBar = QtWidgets.QPlainTextEdit(self.chatPage)
        self.MessageBar.setGeometry(QtCore.QRect(190, 520, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MessageBar.setFont(font)
        self.MessageBar.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.MessageBar.setPlainText("")
        self.MessageBar.setObjectName("MessageBar")
        self.pushButton_3 = QtWidgets.QPushButton(self.chatPage)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 520, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(183, 248, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.chatPage)
        self.textBrowser.setGeometry(QtCore.QRect(190, 70, 581, 441))
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 441))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 441))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(106, 214, 159);\n"
"")
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.curr_chat_label = QtWidgets.QLabel(self.chatPage)
        self.curr_chat_label.setGeometry(QtCore.QRect(320, 30, 271, 31))
        self.curr_chat_label.setAutoFillBackground(False)
        self.curr_chat_label.setStyleSheet("color:rgb(224, 27, 36);")
        self.curr_chat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_chat_label.setObjectName("curr_chat_label")
        self.label_2 = QtWidgets.QLabel(self.chatPage)
        self.label_2.setGeometry(QtCore.QRect(400, 0, 101, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.chatPage)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 101, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.chatPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.LoginButton.clicked.connect(MainWindow.LoginButtonClick) # type: ignore
        self.pushButton.clicked.connect(MainWindow.LabelAppear) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.LabelHide) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.SendMessage) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.LoginButton.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton.setText(_translate("MainWindow", "Priručnik za korištenje"))
        self.pushButton_2.setText(_translate("MainWindow", "Zatvori"))
        self.label_5.setText(_translate("MainWindow", "VacAp - Čet aplikacija"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.curr_chat_label.setText(_translate("MainWindow", "Chat Not Selected"))
        self.label_2.setText(_translate("MainWindow", "Current chat"))
        self.label_3.setText(_translate("MainWindow", "User List"))
