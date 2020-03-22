from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot


class MyWin(QtWidgets.QWidget):
    def __init__(self, parant=None):
        QtWidgets.QWidget.__init__(self, parant)
        self.resize(400, 500)

        self.label = QtWidgets.QLabel('Hello!')
        self.button = QtWidgets.QPushButton('&Click')
        self.button.resize(self.button.sizeHint())
        # self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.button.clicked.connect(self.on_clicked)

        self.gd_main = QtWidgets.QGridLayout(self)
        self.gd_main.addWidget(self.label)
        self.gd_main.addWidget(self.button)

        # self.setWindowIcon(QtGui.QIcon('icon.png'))

        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget.')
        self.button.setToolTip('This is a <b>QPushButton</b> widget.')

    @pyqtSlot()
    def on_clicked(self):
        self.label.setText('Text!')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())