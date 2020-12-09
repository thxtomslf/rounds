from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from sys import argv, exit
from random import randint
from UI import Ui_MainWindow


class Rounds(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)

        self.painter = QPainter()

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setBrush(QColor(randint(0, 255),
                                     randint(0, 255), randint(0, 255)))
        diametr = randint(20, 200)
        self.painter.drawEllipse(randint(0, 700), randint(0, 500),
                                 diametr, diametr)
        self.painter.end()

    def paint(self):
        self.update()


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(argv)
        widg = Rounds()
        widg.show()
        exit(app.exec())