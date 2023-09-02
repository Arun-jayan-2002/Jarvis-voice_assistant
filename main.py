import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import psutil

from mainfile import Ui_Widget

class maingui(QWidget):
    def __init__(self):
        super(maingui, self).__init__()
        print("maingui")
        self.firstUI = Ui_Widget()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("C:\\Users\\arunj\\PycharmProjects\\Jarvis1\\GUI files\\start1.gif")
        self.firstUI.label_2.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.exit.clicked.connect(self.close)
        self.firstUI.start.clicked.connect(self.JARVIS)


    def JARVIS(self):
        from jarvismain import Ui_JARVIS
        self.showjarvismainfile = Ui_JARVIS()
        ui.close()
        self.showjarvismainfile.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = maingui()
    ui.show()
    sys.exit(app.exec_())