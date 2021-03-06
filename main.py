
# Project: Todo list
# Author: Tom Alexa

import sys
from PyQt5 import QtWidgets
from src.database.database import create_tables
from src.gui.window import Ui_MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    create_tables()

    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
