from PyQt5 import QtWidgets, QtCore, QtGui


#
# def window():
#     app = QtWidgets.QApplication(sys.argv)
#     window = QtWidgets.QWidget()
#     window.setWindowTitle('My Window')
#     window.setGeometry(50, 150, 500, 500)
#
#     window.show()
#     sys.exc_info(app.exec_())
#
#
# window()
class MyWin(QtWidgets.QWidget):
    def __init__(self, parant=None):
        QtWidgets.QWidget.__init__(self, parant)
        self.label = QtWidgets.QLabel('Hello!')
        self.button = QtWidgets.QPushButton('&Click')
        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.button)
        self.setLayout(self.v_box)

        # self.setWindowIcon(QtGui.QIcon('icon.png'))

        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget.')
        self.button.setToolTip('This is a <b>QPushButton</b> widget.')

    def clicked(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MyWin()
    win.setWindowTitle('title')
    win.resize(300, 100)
    win.show()
    sys.exit(app.exec_())