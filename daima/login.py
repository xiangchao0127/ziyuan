import json
import os
import re
import sys

import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import  QMainWindow

from qt import query_window

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from login_ui import Ui_MainWindow


class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.loginButton.clicked.connect(self.Login)
        # self.ui.password.textChanged.connect(self.password)
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
    def password(self):
        c2 = self.ui.password.text()
        strinfo = re.compile('\S')
        d2 = strinfo.sub('*', c2, )
        self.ui.password.setText(d2)
    def Login(self):
        # 调用接口
        print(self.ui.username.text().strip(), self.ui.password.text().strip())
        post = requests.post(
            "http://192.168.2.206:8051/user/ExistAccountPassword?Account=" + self.ui.username.text().strip() + "&Password=" + self.ui.password.text().strip())
        success = json.loads(post.text)['data'][0]['code'] == '00'
        if success:
            qt.show()
            self.close()
        else:
            self.ui.error.show()
            print('login fail')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = login_window()
    qt = query_window()
    window.show()
    sys.exit(app.exec_())
