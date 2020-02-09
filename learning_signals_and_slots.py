import sys
from PySide2 import QtWidgets, QtCore, QtGui


class LCDCounter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # LCD display
        lcd = QtWidgets.QLCDNumber(2)

        # Increment buttons
        button_up = QtWidgets.QPushButton("+1")
        button_down = QtWidgets.QPushButton("-1")

        # Set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(button_up)
        layout.addWidget(button_down)
        self.setLayout(layout)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Quit button
        quit = QtWidgets.QPushButton("&Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        # LCD counter
        lcd_counter = LCDCounter()

        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addWidget(lcd_counter)
        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
