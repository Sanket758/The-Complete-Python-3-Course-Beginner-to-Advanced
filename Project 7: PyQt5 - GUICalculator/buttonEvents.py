import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit)


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Let's create some widgets
        label = QLabel("Enter Name")
        name = QLineEdit()
        ok = QPushButton("Ok")
        cancel = QPushButton("Cancel")

        # Create handlers for buttons
        ok.clicked.connect(self.okClicked)
        cancel.clicked.connect(self.CancelClicked)

        # Lets create a layout
        horizontal = QHBoxLayout()

        # We will ad ok and cancel button to horizontal layout so that they will come horizontally next to each other
        horizontal.addWidget(ok)
        horizontal.addWidget(cancel)

        # We will Create an another layout, this will be a vertical layout
        vertical = QVBoxLayout()

        # We will add Label to this one
        vertical.addWidget(label)
        vertical.addWidget(name)
        # Now this is a fun part, you can play around this as you want
        # We are gonna add horizontal layout to our vertical, you can try to add vertical to horizontal, horizontal to horizontal or vertical to vertical
        vertical.addLayout(horizontal)

        # and now we are gonna send our layout2 which is a vertical layout to our mainpage
        self.setLayout(vertical)

        # Lets create a windows title, this is the which will be shown it title bar of our app
        self.setWindowTitle("InputBox")

        # Finally the most important line
        self.show()

    @staticmethod
    def okClicked():
        print('You Clicked Ok!')

    @staticmethod
    def CancelClicked():
        print('You Clicked Cancel!')


if __name__ == "__main__":
    # First we create an app
    app = QApplication(sys.argv)
    # We are gonna call our class here
    window = MainPage()

    # To run our app do:
    sys.exit(app.exec_())
# Done That's your first QT5 app in python
