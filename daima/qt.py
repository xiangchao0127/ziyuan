import shutil
import sys, os
import threading

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets
import sys
from ui_main import Ui_MainWindow
import spider


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # self.tableview = TableView(self)
        self.datas = set()
        self.file = []
        self.fileDest = ""
        self._proxyIp = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.ui.startButton.clicked.connect(self.handle)
        self.ui.youdao.clicked.connect(self.youdao)
        self.ui.bing.clicked.connect(self.bing)
        self.ui.aiciba.clicked.connect(self.aiciba)
        # self.ui.proxy_button.clicked.connect(self.proxyIp)
        self.ui.destFileButton.clicked.connect(self.destFile)
        self.ui.uploadFileButton.clicked.connect(self.chooseFile)
        # self.ui.downloadFile.clicked.connect(self.downloadFile)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.closeButton_2.clicked.connect(self.showMinimized)
        # 给button 的 点击动作绑定一个事件处理函数

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

    # 异步线程回调函数
    def callback(self, name):
        print(name + "语料爬取完成")
        self.ui.state.setText(name + "语料爬取完成")
        self.ui.state.show()


    def bing(self):
        # self.ui.list_view.show()
        self.model = 'bing'

        print(self.model)

    def youdao(self):
        self.model = 'youdao'
        print(self.model)

    def aiciba(self):
        self.model = 'aiciba'
        print(self.model)

    def handle(self):
        # 异步调用
        # _thread.start_new_thread(self.run)
        proxies = {}
        # if self.ui.proxy.text():
        #     proxies = {
        #         "http": self.ui.lineEdit.text(),
        #         "https": self.ui.lineEdit.text(),
        #     }
        keywords = self.ui.keywordsText.toPlainText();
        words = keywords.split(",")
        if self.file:
            words = self.file
        try:
            if hasattr(spider, self.model):
                func = getattr(spider, self.model)
                # func(words)
        except:
            print("请选择模板")
            QMessageBox.information(self,
                                    "消息框标题",
                                    "请选择模板",
                                    QMessageBox.Yes | QMessageBox.No)
            return
        mythread = threading.Thread(target=func, args=(words, proxies,self.fileDest, self))
        mythread.start()
        self.ui.state.setText("爬取状态：进行中，请耐心等待...")
        self.ui.state.show()
        # self.run()

    def proxyIp(self):
        ip, ok = QInputDialog.getMultiLineText(self, "代理", "请输入地址:", "http://username:password@t.16yun.cn:31111")
        proxies = {
            "http": ip,
            "https": ip,
        }
        if ok:
            self._proxyIp = proxies

    def chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            self.file.clear()
            print("\n取消选择")
            return
        print(fileName_choose)
        # self.ui.destFileText.setText(fileName_choose)
        filewords = set()
        with open(fileName_choose, 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                filewords.add(i.strip())
        self.file = list(filewords)

    def downloadFile(self):
        shutil.copy("model.txt", "关键词模板.txt")
    def destFile(self):
        fileDest = QFileDialog.getExistingDirectory(None, "选择存储文件夹",os.getcwd())
        self.fileDest = fileDest+"/"
        self.ui.destFileText.setText(fileDest)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())
