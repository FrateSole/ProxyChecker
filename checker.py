from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.good_proxies = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 562)
        MainWindow.setMinimumSize(QtCore.QSize(873, 562))
        MainWindow.setMaximumSize(QtCore.QSize(873, 562))
        MainWindow.setWindowIcon(QtGui.QIcon("FrateSole.jpg"))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("background-color: rgb(53, 12, 71); color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.proxy_input = QtWidgets.QTextEdit(self.centralwidget)
        self.proxy_input.setGeometry(QtCore.QRect(20, 70, 551, 421))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.proxy_input.setFont(font)
        self.proxy_input.setStyleSheet("color: #FFFFFF;padding: 10px;border-radius: 10px;border: 1px solid rgb(21, 13, 80); background-color: rgb(58, 9, 71)")
        self.proxy_input.setPlaceholderText("ip:port or ip:port:user:pass")
        self.proxy_input.setObjectName("proxy_input")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(350, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: white;background: transparent;")
        self.Title.setObjectName("Title")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(650, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet("color: white;\n"
            "border-radius: 20px;\n"
            "background-color: red;\n"
            "border: 1px solid rgb(21, 13, 80)")
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.hide()
        self.stop_btn.clicked.connect(self.killthread)
        
        
        self.check_btn = QtWidgets.QPushButton(self.centralwidget)
        self.check_btn.setGeometry(QtCore.QRect(650, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.check_btn.setFont(font)
        self.check_btn.setStyleSheet("color: white;\n"
"border-radius: 20px;\n"
"background-color: rgb(8, 126, 0);\n"
"border: 1px solid rgb(21, 13, 80)")
        self.check_btn.setObjectName("check_btn")
        self.check_btn.clicked.connect(self.check)
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(750, 530, 111, 20))
        self.credits.setStyleSheet("color: white;\n"
"background: transparent;")
        self.credits.setObjectName("credits")
        #self.n_threads_box = QtWidgets.QSpinBox(self.centralwidget)
        #self.n_threads_box.setGeometry(QtCore.QRect(660, 230, 111, 31))
        #font = QtGui.QFont()
        #font.setFamily("Verdana")
        #font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        #self.n_threads_box.setFont(font)
        #self.n_threads_box.setStyleSheet("background-color: rgb(58, 9, 71); border-radius: 15px; border: 1px solid rgb(21, 13, 80);")
        #self.n_threads_box.setAlignment(QtCore.Qt.AlignCenter)
        #self.n_threads_box.setObjectName("n_threads_box")
        #self.n_threads_box.setMinimum(1)
        #self.n_threads_box.setMaximum(10)
        self.website_header = QtWidgets.QLabel(self.centralwidget)
        self.website_header.setGeometry(QtCore.QRect(630, 190, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.website_header.setFont(font)
        self.website_header.setStyleSheet("background: transparent")
        self.website_header.setObjectName("website_header")
        self.website_input = QtWidgets.QLineEdit(self.centralwidget)
        self.website_input.setGeometry(QtCore.QRect(610, 230, 221, 21))
        self.website_input.setStyleSheet("border-radius: 10px; background-color:  rgb(58, 9, 71);border: 1px solid rgb(21, 13, 80);")
        self.website_input.setObjectName("website_input")
        
        self.alert_header = QtWidgets.QLabel(self.centralwidget)
        self.alert_header.setGeometry(QtCore.QRect(665, 380, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.alert_header.setFont(font)
        self.alert_header.setStyleSheet("background: transparent; color: red")
        self.alert_header.setObjectName("alert_header")
        
        # self.threads_header = QtWidgets.QLabel(self.centralwidget)
        # self.threads_header.setGeometry(QtCore.QRect(620, 190, 201, 21))
        # font = QtGui.QFont()
        # font.setFamily("Verdana")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.threads_header.setFont(font)
        # self.threads_header.setStyleSheet("background: transparent")
        # self.threads_header.setObjectName("threads_header")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(120, 520, 361, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.status_working = QtWidgets.QLabel(self.splitter)
        self.status_working.setStyleSheet("background: transparent;color: green")
        self.status_working.setObjectName("status_working")
        self.status_notworking = QtWidgets.QLabel(self.splitter)
        self.status_notworking.setStyleSheet("background: transparent;color: red")
        self.status_notworking.setObjectName("status_notworking")
        #just for fun
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(840, 10, 15, 15))
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setStyleSheet("""
        background-color:#e4685d;
        border-radius:7px;
        font-family:Verdana;
        font-size:12px;""")
        self.close_btn.setText("X")
        self.close_btn.clicked.connect(QtWidgets.qApp.quit)

        self.resize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.resize_btn.setGeometry(QtCore.QRect(800, 10, 15, 15))
        self.resize_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resize_btn.setStyleSheet("""
        background-color:#FFFF00;
        border-radius:7px;
        font-family:Verdana;
        font-size:12px;""")
        self.resize_btn.setText("-")
        self.resize_btn.clicked.connect(self.resize)
        #just for fun
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proxy Checker"))
        self.Title.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#00e4f0;\">ProxyChecker</span></p></body></html>"))
        self.Title.setText(_translate("MainWindow", "Proxy Checker"))
        self.check_btn.setText(_translate("MainWindow", "Check"))
        self.credits.setText(_translate("MainWindow", "GitHub > @FrateSole"))
        self.website_header.setText(_translate("MainWindow", "Website to check proxy"))
        self.status_working.setText(_translate("MainWindow", "working: 0"))
        self.status_notworking.setText(_translate("MainWindow", "not-working: 0"))
        self.alert_header.setText(_translate("MainWindow", ""))
        self.stop_btn.setText(_translate("MainWindow", "STOP"))
    def resize(self):
        MainWindow.showMinimized()
        return
    def check(self):
        website = self.website_input.text()
        #n_threads = self.n_threads_box.value()
        proxies_to_split = self.proxy_input.toPlainText()
        if website == "":
            self.alert_header.setText("Invalid website")
        elif proxies_to_split == "":
            self.alert_header.setText("Invalid Proxies")
        if website != "" and proxies_to_split != "":
            for item in proxies_to_split.splitlines():
                if ":" not in item or item == "":
                    self.alert_header.setText("Invalid Proxies")
                    return
            self.thread = Thread(website, proxies_to_split)
            self.thread.working.connect(self.working)
            self.thread.not_working.connect(self.not_working)
            self.thread.done.connect(self.done)
            self.thread.start()
            self.stop_btn.show()
            self.check_btn.hide()
            self.alert_header.setStyleSheet("color: green")
            self.alert_header.setText("Checking...")
            
    def killthread(self):
        self.thread.stop()
        self.stop_btn.hide()
        self.check_btn.show()
        self.alert_header.setText("")
        str1 = "\n"
        a = str1.join(self.good_proxies)
        self.proxy_input.setText(a)
    def working(self, a, i):
        self.status_working.setText("working: " + str(a))
        self.good_proxies.append(i)
        return
    def not_working(self, b):
        self.status_notworking.setText("not-working: " + str(b))
        return
    def done(self):
        self.thread.stop()
        self.stop_btn.hide()
        self.check_btn.show()
        self.alert_header.setText("DONE")
        str1 = "\n"
        a = str1.join(self.good_proxies)
        self.proxy_input.setText(a)
        return
                    
class Thread(QtCore.QThread):
    working = QtCore.pyqtSignal('PyQt_PyObject')
    not_working = QtCore.pyqtSignal('PyQt_PyObject')
    done = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self, website, proxies_to_split):
        self.website, self.proxies_to_split = website, proxies_to_split
        QtCore.QThread.__init__(self)
        self.threadactive = True
        
    def run(self):
        a = 0
        b = 0
        for i in self.proxies_to_split.splitlines():
            while self.threadactive:
                try:
                    proxy_parts = i.split(":")
                    ip, port, user, passw = proxy_parts[0], proxy_parts[1], proxy_parts[2], proxy_parts[3]
                    proxy = {
                    "http": "http://{}:{}@{}:{}".format(user, passw, ip, port),
                    "https": "https://{}:{}@{}:{}".format(user, passw, ip, port)
                    }
                except IndexError:
                    try:
                        proxy =  {"http": "http://" + i, "https": "https://" + i}
                    except:
                        pass
                
                HEADERS = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                session = requests.session()
                session.headers.update(HEADERS)
                try:
                    response = session.get(self.website, proxies=proxy)
                    if response.status_code in (200, 302, 300):
                        a += 1
                        self.working.emit(a, i)
                        break
                    else:
                        b += 1
                        self.not_working.emit(b)
                        break
                except:
                    b += 1
                    self.not_working.emit(b)
                    break
        self.done.emit(self)
    def stop(self):
        self.threadactive = False
        self.wait()           
                    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #ui.setWindowIcon(QtGui.QIcon("Frate.png"))
    sys.exit(app.exec_())
