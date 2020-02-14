import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Button:
    def __init__(self, text, results):
        self.but = QPushButton(str(text))
        self.text = text
        self.results = results
        self.but.clicked.connect(lambda: self.inputHandler(self.text))

    def inputHandler(self, t):
        if t == '=':
            result = eval(self.results.text())
            self.results.setText(str(result))
        elif t == 'AC':
            self.results.setText("")
        elif t == '√':
            current_val = float(self.results.text())
            self.results.setText(str(math.sqrt(current_val)))
        elif t == 'DEL':
            current_val = self.results.text()
            self.results.setText(current_val[:-1])
        else:
            current_val = self.results.text()
            new_val = current_val + str(t)
            self.results.setText(new_val)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.init_gui()

    def init_gui(self):
        Grid = QGridLayout()
        query = QLineEdit()
        buttons = ["AC", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        row = 1
        col = 0
        Grid.addWidget(query, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            buttonObj = Button(button, query)
            if button == 0:
                Grid.addWidget(buttonObj.but, row, col, 1, 2)
                col += 1
            else:
                Grid.addWidget(buttonObj.but, row, col, 1, 1)
            col += 1

        self.setLayout(Grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
