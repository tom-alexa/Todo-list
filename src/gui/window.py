
from datetime import date, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 390, 370))
        self.listWidget.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 20px;")
        self.listWidget.setObjectName("listWidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(470, 100, 320, 470))
        self.widget_2.setStyleSheet("background-color: rgb(54, 21, 0);")
        self.widget_2.setObjectName("widget_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 60, 280, 370))
        self.listWidget_2.setStyleSheet("background-color: rgb(96, 54, 1);\n"
"border-radius: 20px;")
        self.listWidget_2.setObjectName("listWidget_2")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        day_1 = date.today() - timedelta(days=2)
        day_2 = date.today() - timedelta(days=1)
        day_3 = date.today()
        day_4 = date.today() + timedelta(days=1)
        day_5 = date.today() + timedelta(days=2)
        day_6 = date.today() + timedelta(days=3)
        day_7 = date.today() + timedelta(days=4)
        day_8 = date.today() + timedelta(days=5)

        MainWindow.setWindowTitle(_translate("MainWindow", "Todo list"))
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
