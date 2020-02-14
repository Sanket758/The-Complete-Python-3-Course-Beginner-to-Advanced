import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GridLayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        # Lets create a windows title, this is the which will be shown it title bar of our app
        self.setWindowTitle("Grid Layout")
        self.init_ui()

    def init_ui(self):

        # Lets create a layout
        Grid = QGridLayout()

        # Let's create some widgets
        Button1 = QPushButton("Button 1")
        Button2 = QPushButton("Button 2")
        Button3 = QPushButton("Button 3")
        Button4 = QPushButton("Button 4")

        # Grid Layout will take 4 positional args: first two are the rows and columns and next two are the size.
        Grid.addWidget(Button1, 0, 0, 1, 1)
        Grid.addWidget(Button2, 0, 1, 1, 1)
        Grid.addWidget(Button3, 0, 2, 1, 1)
        Grid.addWidget(Button4, 1, 0, 1, 2)

        # and now we are gonna send our Grid layout to our mainpage
        self.setLayout(Grid)

        # Finally the most important line
        self.show()


if __name__ == "__main__":
    # First we create an app
    app = QApplication(sys.argv)
    # We are gonna call our class here
    window = GridLayoutDemo()

    # To run our app do:
    sys.exit(app.exec_())

