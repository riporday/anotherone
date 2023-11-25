import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None
        self.pushButton.clicked.connect(self.mousePressEvent)

    def initUI(self):
        self.setWindowTitle('Рисование')


    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = randint(20, 100)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                            int(self.coords_[1] - R / 2), R, R)


    def mousePressEvent(self, event):
        self.coords_ = [177, 100]
        self.status = 1
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())
