import sys
from PySide2 import QtWidgets, QtCore, QtGui


class LCDCounter(QtWidgets.QWidget):
    def __init__(self, initial_value, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.value = initial_value

        # LCD display
        self.lcd = QtWidgets.QLCDNumber(2)
        self.lcd.display(self.value)

        # Increment buttons
        self.button_up = QtWidgets.QPushButton("+1")
        self.button_down = QtWidgets.QPushButton("-1")

        # Connections
        self.connect(self.button_up, QtCore.SIGNAL("clicked()"),
                     self.add_one)
        self.connect(self.button_down, QtCore.SIGNAL("clicked()"),
                     self.minus_one)

        # Set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.button_up)
        layout.addWidget(self.button_down)
        self.setLayout(layout)

    @QtCore.Slot()
    def add_one(self):
        self.value += 1
        print(self.value)
        self.lcd.display(self.value)

    @QtCore.Slot()
    def minus_one(self):
        self.value -= 1
        print(self.value)
        self.lcd.display(self.value)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Quit button
        quit = QtWidgets.QPushButton("&Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        # LCD counter
        lcd_counter = LCDCounter(35)

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
