import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5 import uic

#from main_window_ui import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        root = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(root, 'main_window.ui'), self)
        self.show()
    
    def btnClick(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % self.stackedWidget.count())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())