import sys
from PySide2 import QtWidgets, QtCore, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

        grid = QtWidgets.QGridLayout()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
