from PyQt5 import QtCore, QtWidgets, uic, QtWebEngineWidgets
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
        url = QUrl("file:///media/nadir/data/scripts/qtwebengine_ckeditor/index.html")
        self.browser.page().load(url)
        self.btnSaveToFile.clicked.connect(self.btnsavedtofile)
        self.btnLoadFromFile.clicked.connect(self.btnloadfromfile)

    def btnsavedtofile(self):
        def callbackfunction(re):
            print(re)
        print(self.browser.page().runJavaScript("CKEDITOR.instances.editor.getData();", callbackfunction))

        # self.browser.page().runJavaScript("CKEDITOR.instances.editor.resize( '100%', '350', true );", callbackfunction)
        print('its work')

    def btnloadfromfile(self):
        def callbackfunction(re):
            print(re)
        s = ''   
        with open('/media/nadir/data/scripts/qtwebengine_ckeditor/files/banka_fisi.html', 'r') as f:
            s = f.read()

        print(s)
            

        self.browser.page().runJavaScript("CKEDITOR.instances.editor.setData('%s');" % s, callbackfunction)
 
        print('its work')

if __name__ == "__main__":
    view = MainWindow()
    view.show()
    #app.exec_()
    reactor.run()
