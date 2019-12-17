# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 307)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255);\n"
                                 "\n"
                                 "")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(80, 80, 302, 38))
        self.username.setStyleSheet("font: 10pt \"微软雅黑\";\n"
                                    "")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 140, 302, 38))
        self.password.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(80, 220, 302, 38))
        self.loginButton.setStyleSheet("color:rgb(255, 255, 255);\n"
                                       "background: rgb(20, 147, 151);\n"
                                       "\n"
                                       "font: 10pt \"微软雅黑\";\n"
                                       "")
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 90, 29, 21))
        self.label.setPixmap(QtGui.QPixmap("PyQt5/Qt/image/user.png"))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 29, 20))
        self.label_2.setPixmap(QtGui.QPixmap("PyQt5/Qt/image/pass.png"))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 461, 41))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "\n"
                                   "background: rgb(20, 147, 151);\n"
                                   "\n"
                                   "font: 10pt \"微软雅黑\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(18, 10, 54, 21))
        self.label_4.setStyleSheet("background: rgba（0,0,0,0）;\n"
                                   "image: url(:/newPrefix/logo_16x16.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("PyQt5/Qt/image/logo_16x16.png"))
        self.label_4.setObjectName("label_4")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(410, 10, 41, 23))
        self.closeButton.setStyleSheet("border:none;\n"
                                       "image: url(:/newPrefix/close_16x16.png);\n"
                                       "background: rgb(20, 147, 151);")
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PyQt5/Qt/image/close_16x16.png"), QtGui.QIcon.Normal)
        self.closeButton.setIcon(icon)
        self.closeButton.setObjectName("closeButton")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(180, 190, 91, 21))
        self.error.setStyleSheet("background:rgb(255,255,255);\n"
                                 "color:  rgb(20, 147, 151);\n"
                                 "font: 10pt \"微软雅黑\";")
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "语料采集工具v1.0版本 - 登录"))
        self.username.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.password.setPlaceholderText(_translate("MainWindow", "密码"))
        # self.username.setText("          ")
        # self.password.setText("          ")
        self.loginButton.setText(_translate("MainWindow", "登 录"))
        self.label_3.setText(_translate("MainWindow", "          语料采集工具v1.0版本 - 登录"))
        self.error.setText(_translate("MainWindow", "用户名密码错误"))
        self.password.setEchoMode(QLineEdit.Password)
        self.error.hide()
if __name__ == '__main__':
    c2 = '   world'
    strinfo = re.compile('\S')
    d2 = strinfo.sub('*', c2, )
    print('2原始字符串:{}'.format(c2))
    print('2替换字符串:{}'.format(d2))

