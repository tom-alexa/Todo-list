
from datetime import date, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from src.database.database import select_items, insert_item


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(28, 10, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.date = QtWidgets.QWidget(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(0, 0, 802, 80))
        self.date.setStyleSheet("")
        self.date.setObjectName("date")
        self.day_1 = QtWidgets.QPushButton(self.date)
        self.day_1.setGeometry(QtCore.QRect(5, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_1.setFont(font)
        self.day_1.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_1.setObjectName("day_1")
        self.day_2 = QtWidgets.QPushButton(self.date)
        self.day_2.setGeometry(QtCore.QRect(105, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_2.setFont(font)
        self.day_2.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_2.setObjectName("day_2")
        self.day_3 = QtWidgets.QPushButton(self.date)
        self.day_3.setGeometry(QtCore.QRect(205, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_3.setFont(font)
        self.day_3.setStyleSheet("background-color: rgb(96, 54, 1);")
        self.day_3.setObjectName("day_3")
        self.day_4 = QtWidgets.QPushButton(self.date)
        self.day_4.setGeometry(QtCore.QRect(305, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_4.setFont(font)
        self.day_4.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_4.setObjectName("day_4")
        self.day_6 = QtWidgets.QPushButton(self.date)
        self.day_6.setGeometry(QtCore.QRect(505, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_6.setFont(font)
        self.day_6.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_6.setObjectName("day_6")
        self.day_5 = QtWidgets.QPushButton(self.date)
        self.day_5.setGeometry(QtCore.QRect(405, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_5.setFont(font)
        self.day_5.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_5.setObjectName("day_5")
        self.day_7 = QtWidgets.QPushButton(self.date)
        self.day_7.setGeometry(QtCore.QRect(605, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_7.setFont(font)
        self.day_7.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_7.setObjectName("day_7")
        self.day_8 = QtWidgets.QPushButton(self.date)
        self.day_8.setGeometry(QtCore.QRect(705, 10, 90, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.day_8.setFont(font)
        self.day_8.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.day_8.setObjectName("day_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 100, 450, 470))
        self.widget.setStyleSheet("background-color: rgb(54, 21, 0);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 390, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.list_of_items = QtWidgets.QListWidget(self.widget)
        self.list_of_items.setGeometry(QtCore.QRect(40, 60, 390, 370))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.list_of_items.setFont(font)
        self.list_of_items.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 10px;\n"
"padding: 20px")
        self.list_of_items.setObjectName("list_of_items")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(470, 100, 320, 470))
        self.widget_2.setStyleSheet("background-color: rgb(54, 21, 0);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.add_item_widget = QtWidgets.QWidget(self.widget_2)
        self.add_item_widget.setGeometry(QtCore.QRect(20, 60, 280, 370))
        self.add_item_widget.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 10px;")
        self.add_item_widget.setObjectName("add_item_widget")
        self.label_3 = QtWidgets.QLabel(self.add_item_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.add_item_widget)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.add_item_widget)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.add_item_widget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 121, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.add_item_widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 200, 241, 81))
        self.textEdit.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.textEdit.setObjectName("textEdit")
        self.add_button = QtWidgets.QPushButton(self.add_item_widget)
        self.add_button.setGeometry(QtCore.QRect(210, 300, 51, 51))
        self.add_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(115, 210, 22);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(78, 154, 6)\n"
"}")
        self.add_button.setObjectName("pushButton")
        self.dateEdit = QtWidgets.QDateEdit(self.add_item_widget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 30, 121, 41))
        self.dateEdit.setStyleSheet("background-color: rgb(204, 149, 68);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.active_day = date.today()

        self.retranslateUi(MainWindow)
        self.load_items()
        self.connect_buttons()
        self.set_input_values()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todo list"))
        self.translate_buttons()
        self.translate_add()


    def translate_buttons(self):
        _translate = QtCore.QCoreApplication.translate

        day_1 = date.today() - timedelta(days=2)
        day_2 = date.today() - timedelta(days=1)
        day_3 = date.today()
        day_4 = date.today() + timedelta(days=1)
        day_5 = date.today() + timedelta(days=2)
        day_6 = date.today() + timedelta(days=3)
        day_7 = date.today() + timedelta(days=4)
        day_8 = date.today() + timedelta(days=5)

        day, month = day_1.day, day_1.month
        self.day_1.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_2.day, day_2.month
        self.day_2.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_3.day, day_3.month
        self.day_3.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_4.day, day_4.month
        self.day_4.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_5.day, day_5.month
        self.day_5.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_6.day, day_6.month
        self.day_6.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_7.day, day_7.month
        self.day_7.setText(_translate("MainWindow", f"{day}.{month}."))
        day, month = day_8.day, day_8.month
        self.day_8.setText(_translate("MainWindow", f"{day}.{month}."))

        day, month, year = self.active_day.day, self.active_day.month, self.active_day.year
        self.label.setText(_translate("MainWindow", f"{day}.{month}.{year}"))
        self.label_2.setText(_translate("MainWindow", "Add"))


    def translate_add(self):
        _translate = QtCore.QCoreApplication.translate

        self.label.setText(_translate("MainWindow", "1.1.2022"))
        self.label_2.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Date"))
        self.label_6.setText(_translate("MainWindow", "Title"))
        self.label_7.setText(_translate("MainWindow", "Description"))
        self.add_button.setText(_translate("MainWindow", "Add"))


    def set_input_values(self):
        self.lineEdit.clear()
        self.textEdit.clear()
        self.dateEdit.setDate(self.active_day)


    def load_items(self):
        items = select_items(self.active_day)
        self.list_of_items.clear()
        for item in items:
            list_item = QtWidgets.QListWidgetItem(self.list_of_items)
            text_to_view = "{}\n    {}".format(item[3], item[4].replace("\n", "\n    "))
            list_item.setText(text_to_view)


    def connect_buttons(self):
        self.day_1.clicked.connect(lambda: self.set_active_day(-2))
        self.day_2.clicked.connect(lambda: self.set_active_day(-1))
        self.day_3.clicked.connect(lambda: self.set_active_day(0))
        self.day_4.clicked.connect(lambda: self.set_active_day(1))
        self.day_5.clicked.connect(lambda: self.set_active_day(2))
        self.day_6.clicked.connect(lambda: self.set_active_day(3))
        self.day_7.clicked.connect(lambda: self.set_active_day(4))
        self.day_8.clicked.connect(lambda: self.set_active_day(5))

        self.add_button.clicked.connect(lambda: self.add_item(self.lineEdit.text(), self.textEdit.toPlainText(), self.dateEdit.text()))


    def set_active_day(self, diff):
        self.active_day = date.today() + timedelta(diff)
        self.translate_buttons()
        self.load_items()


    def add_item(self, title, description, in_date):
        self.set_input_values()
        if not title:
            return
        d = in_date.split("/")
        year = d[2]
        month = d[1]
        day = d[0]
        insert_item(title, description, f"{year}-{month}-{day}")
        self.load_items()
