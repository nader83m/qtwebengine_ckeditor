from PyQt5 import QtCore, QtWidgets, uic, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
app = QApplication([])
import qt5reactor
qt5reactor.install()
from twisted.internet import defer, reactor
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainWindow.ui', self)
        self.showMaximized()

        # self.showFullScreen()
        self.path = os.getcwd()
        url = QUrl("file://%s/index.html" % self.path)
        self.browser.page().load(url)
        self.btnSaveToFile.clicked.connect(self.btnsavedtofile)
        self.btnLoadFromFile.clicked.connect(self.btnloadfromfile)

    def btnsavedtofile(self):
        def callbackfunction(re):
            with open('%s/files/out.html' % self.path, 'w') as f:
                s = f.write(re)
        print(self.browser.page().runJavaScript("CKEDITOR.instances.editor.getData();", callbackfunction))
        # self.browser.page().runJavaScript("CKEDITOR.instances.editor.resize( '100%', '350', true );", callbackfunction)

    def btnloadfromfile(self):
        def callbackfunction(re):
            pass
        s = ''
        with open('%s/files/input.html' % self.path, 'r') as f:
            s = f.read()

        self.browser.page().runJavaScript("CKEDITOR.instances.editor.setData(`%s`);" % s, callbackfunction)
 
if __name__ == "__main__":
    view = MainWindow()
    view.show()
    #app.exec_()
    reactor.run()
