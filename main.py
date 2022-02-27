
# Project: Todo list
# Author: Tom Alexa

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()

    width, height = 600, 500
    win.setFixedWidth(width)
    win.setFixedHeight(height)
    win.setWindowTitle("Todo list")

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
