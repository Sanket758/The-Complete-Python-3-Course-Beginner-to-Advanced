import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Let's create some widgets
        label = QLabel("Hi There")
        ok = QPushButton("Ok")
        cancel = QPushButton("Cancel")

        # Lets create a layout
        horizontal = QHBoxLayout()
        # This will give ability to resize the window otherwise it would be statick or say fixed size
        horizontal.addStretch()
        # We will ad ok and cancel button to horizontal layout so that they will come horizontally next to each other
        horizontal.addWidget(ok)
        horizontal.addWidget(cancel)

        # We will Create an another layout, this will be a vertical layout
        vertical = QVBoxLayout()
        vertical.addStretch()
        # We will add Label to this one
        vertical.addWidget(label)

        # Now this is a fun part, you can play around this as you want
        # We are gonna add horizontal layout to our vertical, you can try to add vertical to horizontal, horizontal to horizontal or vertical to vertical
        vertical.addLayout(horizontal)

        # and now we are gonna send our layout2 which is a vertical layout to our mainpage
        self.setLayout(vertical)

        # Lets create a windows title, this is the which will be shown it title bar of our app
        self.setWindowTitle("LayoutPlay")

        # Finally the most important line
        self.show()


if __name__ == "__main__":
    # First we create an app
    app = QApplication(sys.argv)
    # We are gonna call our class here
    window = MainPage()

    # To run our app do:
    sys.exit(app.exec_())
# Done That's your first QT5 app in python
