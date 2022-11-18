import sys

from UI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(Ui_Form)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawCircle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0, self.width()), randint(0, self.height()), rad := randint(50, 150), rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
