# PyQt imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os
import sys

class MainWindow(QMainWindow): # Launches a new PyQt container window and loads the Disney+ site.
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView() # starts PyQt web renderer.
        self.browser.setUrl(QUrl("http://disneyplus.com")) # defines site to load and loads it.

        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.show()

        self.setWindowIcon(QIcon(os.path.join('images', 'plus.png'))) # I typed in "blue plus sign" into DuckDuckGo and downloaded a generic, shiny, plus sign.

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s" % title)

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

        self.browser.setUrl(q)

app = QApplication(sys.argv)
app.setApplicationName("Disney+")
app.setOrganizationName("Disney+")
app.setOrganizationDomain("disneyplus.com")

window = MainWindow()

app.exec_()