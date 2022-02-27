# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.day_1.setObjectName("day_1")
        self.day_2 = QtWidgets.QPushButton(self.date)
        self.day_2.setGeometry(QtCore.QRect(105, 10, 90, 60))
        self.day_2.setObjectName("day_2")
        self.day_3 = QtWidgets.QPushButton(self.date)
        self.day_3.setGeometry(QtCore.QRect(205, 10, 90, 60))
        self.day_3.setObjectName("day_3")
        self.day_4 = QtWidgets.QPushButton(self.date)
        self.day_4.setGeometry(QtCore.QRect(305, 10, 90, 60))
        self.day_4.setObjectName("day_4")
        self.day_6 = QtWidgets.QPushButton(self.date)
        self.day_6.setGeometry(QtCore.QRect(505, 10, 90, 60))
        self.day_6.setObjectName("day_6")
        self.day_5 = QtWidgets.QPushButton(self.date)
        self.day_5.setGeometry(QtCore.QRect(405, 10, 90, 60))
        self.day_5.setObjectName("day_5")
        self.day_7 = QtWidgets.QPushButton(self.date)
        self.day_7.setGeometry(QtCore.QRect(605, 10, 90, 60))
        self.day_7.setStyleSheet("")
        self.day_7.setObjectName("day_7")
        self.day_8 = QtWidgets.QPushButton(self.date)
        self.day_8.setGeometry(QtCore.QRect(705, 10, 90, 60))
        self.day_8.setObjectName("day_8")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 100, 400, 440))
        self.listWidget.setStyleSheet("background-color: rgb(54, 21, 0);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(430, 100, 350, 440))
        self.listWidget_2.setStyleSheet("background-color: rgb(54, 21, 0);")
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todo list"))
        self.day_1.setText(_translate("MainWindow", "PushButton"))
        self.day_2.setText(_translate("MainWindow", "PushButton"))
        self.day_3.setText(_translate("MainWindow", "PushButton"))
        self.day_4.setText(_translate("MainWindow", "PushButton"))
        self.day_6.setText(_translate("MainWindow", "PushButton"))
        self.day_5.setText(_translate("MainWindow", "PushButton"))
        self.day_7.setText(_translate("MainWindow", "PushButton"))
        self.day_8.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
