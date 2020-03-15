import sys

from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle('My Window')
    window.setGeometry(50, 150, 500, 500)

    window.show()
    sys.exc_info(app.exec_())


window()
