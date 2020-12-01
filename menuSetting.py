
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
from config import config, confcreate

class MenuSetting(QDialog):
    def __init__(self, parent):
        super(MenuSetting, self).__init__()
        loadUi("gui/settingModel.ui", self)
        self.txtpath.setEnabled(False)
        self.btn_cancel.clicked.connect(self.close)
        self.btnchange.clicked.connect(self.loadFile)
        self.btn_save.clicked.connect(self.saveConf)
    def readConf(self):
        self.path = config()
        self.txtpath.setText(self.path['path'])

    def saveConf(self):
        if len(self.txtpath.text())>0:
            self.lok = self.txtpath.text()
            confcreate(self.lok)
            print('simpan berhasil')

    def loadFile(self):
        self.filename = QFileDialog.getOpenFileName()[0]
        if len(self.filename) > 3:
            self.txtpath.setText(self.filename)
        