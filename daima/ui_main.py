# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 693)
        MainWindow.setStyleSheet("background:rgb(255,255,255)")
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.youdao = QtWidgets.QRadioButton(self.centralwidget)
        self.youdao.setGeometry(QtCore.QRect(90, 60, 89, 16))
        self.youdao.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.youdao.setObjectName("youdao")
        self.bing = QtWidgets.QRadioButton(self.centralwidget)
        self.bing.setGeometry(QtCore.QRect(190, 60, 89, 16))
        self.bing.setObjectName("bing")
        self.aiciba = QtWidgets.QRadioButton(self.centralwidget)
        self.aiciba.setGeometry(QtCore.QRect(280, 60, 89, 16))
        self.aiciba.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.aiciba.setObjectName("aiciba")
        self.other = QtWidgets.QRadioButton(self.centralwidget)
        self.other.setGeometry(QtCore.QRect(380, 60, 89, 16))
        self.other.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.other.setObjectName("other")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 71, 16))
        self.label_2.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.destFileText = QtWidgets.QLineEdit(self.centralwidget)
        self.destFileText.setGeometry(QtCore.QRect(580, 50, 341, 31))
        self.destFileText.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.destFileText.setObjectName("destFileText")
        self.destFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.destFileButton.setGeometry(QtCore.QRect(930, 50, 70, 31))
        self.destFileButton.setStyleSheet("color:rgb(255, 255, 255);\n"
                                          "background: rgb(20, 147, 151);\n"
                                          "font: 9pt \"微软雅黑\";\n"
                                          "")
        self.destFileButton.setObjectName("destFileButton")
        self.keywordsText = QtWidgets.QTextEdit(self.centralwidget)
        self.keywordsText.setGeometry(QtCore.QRect(20, 100, 981, 481))
        self.keywordsText.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.keywordsText.setObjectName("keywordsText")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(920, 590, 81, 31))
        self.startButton.setStyleSheet("color:rgb(255, 255, 255);\n"
                                       "background: rgb(20, 147, 151);\n"
                                       "font: 9pt \"微软雅黑\";\n"
                                       "")
        self.startButton.setObjectName("startButton")
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(720, 600, 201, 21))
        self.state.setStyleSheet("color:rgb(20, 147, 151);\n"
                                 "font: 9pt \"微软雅黑\";")
        self.state.setObjectName("state")
        self.uploadFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadFileButton.setGeometry(QtCore.QRect(40, 530, 75, 31))
        self.uploadFileButton.setStyleSheet("color:rgb(20, 147, 151);\n"
                                            "background : white;\n"
                                            "font: 9pt \"微软雅黑\";")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("PyQt5/Qt/image/upload_16x16.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadFileButton.setIcon(icon)
        self.uploadFileButton.setObjectName("uploadFileButton")
        self.state_2 = QtWidgets.QLabel(self.centralwidget)
        self.state_2.setGeometry(QtCore.QRect(440, 630, 181, 21))
        self.state_2.setStyleSheet("color:rgb(102, 102, 102)")
        self.state_2.setObjectName("state_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1021, 41))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "\n"
                                   "background: rgb(20, 147, 151);\n"
                                   "\n"
                                   "font: 11pt \"微软雅黑\";\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 54, 21))
        self.label_4.setStyleSheet("background: rgba（0,0,0,0）;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("PyQt5/Qt/image/logo_16x16.png"))
        self.label_4.setObjectName("label_4")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(980, 0, 31, 41))
        self.closeButton.setStyleSheet("border:none;\n"
                                       "image: url(:/newPrefix/close_16x16.png);\n"
                                       "background: rgb(20, 147, 151);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PyQt5/Qt/image/close_16x16.png"), QtGui.QIcon.Normal)
        self.closeButton.setIcon(icon)
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.closeButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton_2.setGeometry(QtCore.QRect(950, 0, 31, 41))
        self.closeButton_2.setStyleSheet("border:none;\n"
                                         "image: url(:/newPrefix/hide_16x16.png);\n"
                                         "background: rgb(20, 147, 151);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PyQt5/Qt/image/hide_16x16.png"), QtGui.QIcon.Normal)
        self.closeButton_2.setIcon(icon)
        self.closeButton_2.setText("")
        self.closeButton_2.setObjectName("closeButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "目标选择："))
        self.youdao.setText(_translate("MainWindow", "有道词典"))
        self.bing.setText(_translate("MainWindow", "Bing"))
        self.aiciba.setText(_translate("MainWindow", "爱词霸"))
        self.other.setText(_translate("MainWindow", "其他"))
        self.label_2.setText(_translate("MainWindow", "存放目录："))
        self.destFileButton.setText(_translate("MainWindow", "选择目录"))
        self.keywordsText.setPlaceholderText(_translate("MainWindow", "可在此直接输入想要搜索的关键词，并以“,”(英文逗号)隔开。搜索目标将以文件优先处理"))
        self.startButton.setText(_translate("MainWindow", "开始爬取"))
        self.state.setText(_translate("MainWindow", "爬取状态：进行中，请耐心等待..."))
        self.state.hide()
        self.uploadFileButton.setText(_translate("MainWindow", "上传文件"))
        self.state_2.setText(_translate("MainWindow", "© 四川语言桥信息技术有限公司"))
        self.label_3.setText(_translate("MainWindow", "           语料采集工具v1.0版本"))
