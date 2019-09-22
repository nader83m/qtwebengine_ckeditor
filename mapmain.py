from PyQt5 import QtCore, QtWidgets, uic
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
app = QApplication([])
import qt5reactor
qt5reactor.install()
from twisted.internet import defer, reactor


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainWindow.ui', self)
        url = QUrl("file:///home/nadir/PycharmProjects/pythonckeditor/index.html")
        self.browser.page().load(url)
        self.btnSaveToFile.clicked.connect(self.btnsavedtofile)
        self.btnLoadFromFile.clicked.connect(self.btnloadfromfile)

    def btnsavedtofile(self):

        self.browser.page().runJavaScript()
        print('its work')

    def btnloadfromfile(self):
        print('its work')

if __name__ == "__main__":
    view = MainWindow()
    view.show()
    #app.exec_()
    reactor.run()
