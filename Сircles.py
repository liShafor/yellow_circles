import sys

from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from UI import Ui_MainWindow


class YellowCirclesDraw(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False

        self.setFixedSize(445, 385)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.size = randint(10, 100)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.update()

        self.do_paint = True

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()

            qp.begin(self)

            qp.setBrush(QColor(*self.color))
            qp.setPen(QColor(*self.color))

            self.x, self.y = randint(100, 445 - 100), randint(100, 385 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCirclesDraw()
    ex.show()
    sys.exit(app.exec())