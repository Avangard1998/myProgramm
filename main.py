import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setWindowTitle("Golf")
        self.setFixedSize(1200, 800)

        self.game_text = QtWidgets.QLabel(self)
        self.game_text.setText("Golf")
        self.game_text.setFont(QtGui.QFont("Times", 48, QtGui.QFont.Bold))
        self.game_text.move(500, 200)
        self.game_text.adjustSize()

        self.button_play = QtWidgets.QPushButton(self)
        self.button_play.move(500, 300)
        self.button_play.setFixedSize(100, 50)
        self.button_play.setText("Play")
        #self.button_play.clicked.connect(self.b_play)

        self.button_exit = QtWidgets.QPushButton(self)
        self.button_exit.move(500, 400)
        self.button_exit.setFixedSize(100, 50)
        self.button_exit.setText("Exit")
        self.button_exit.clicked.connect(self.b_exit)
        print("123")

    #def b_play (self):

    def b_exit (self):
        sys.exit()

def menu ():

    menu = QApplication(sys.argv)
    window_menu = window()
    window_menu.show()
    sys.exit(menu.exec_())

if __name__ == "__main__":
    menu()