# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.uic import loadUi
import cv2
import sys
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        loadUi("gui/mainMenu.ui", self)
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(864, 600)
        self.filename = None
        self.image = None
        self.liveStat = False

        self.labelScreen.setStyleSheet("background-color: black")
        self.btnLive.clicked.connect(self.goLive)
        self.btnOpen.clicked.connect(self.loadImage)
        self.model = load_model('models/material.h5')
        self.checkPredict.stateChanged.connect(self.checkstate)
        self.btnPredict.clicked.connect(self.singleImage)
        self.checkPredict.setEnabled(False)
        self.btnPredict.setEnabled(False)

        """
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelScreen = QtWidgets.QLabel(self.centralwidget)
        self.labelScreen.setMinimumSize(QtCore.QSize(600, 0))
        self.labelScreen.setObjectName("labelScreen")
        self.horizontalLayout.addWidget(self.labelScreen)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTgl = QtWidgets.QLabel(self.centralwidget)
        self.labelTgl.setStyleSheet("font: 24pt \".SF NS Text\";")
        self.labelTgl.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTgl.setObjectName("labelTgl")
        self.verticalLayout.addWidget(self.labelTgl)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.labelMaterial = QtWidgets.QLabel(self.centralwidget)
        self.labelMaterial.setStyleSheet("font: 40pt \".SF NS Text\";")
        self.labelMaterial.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMaterial.setObjectName("labelMaterial")
        self.verticalLayout.addWidget(self.labelMaterial)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLive = QtWidgets.QPushButton(self.centralwidget)
        self.btnLive.setObjectName("btnLive")
        self.horizontalLayout_2.addWidget(self.btnLive)
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout_2.addWidget(self.btnOpen)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuMenu.addAction(self.actionOpen_File)
        self.menuMenu.addAction(self.actionClose)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelScreen.setText(_translate("MainWindow", "TextLabel"))
        self.labelTgl.setText(_translate("MainWindow", "Tanggal"))
        self.label_3.setText(_translate("MainWindow", "Jenis Material :"))
        self.labelMaterial.setText(_translate("MainWindow", "TextLabel"))
        self.btnLive.setText(_translate("MainWindow", "LIVE"))
        self.btnOpen.setText(_translate("MainWindow", "OPEN"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    def goLive(self):
        if self.liveStat:
            self.stopLive()
        else:
            self.liveCam()

    def stopLive(self):
        if self.liveStat:
            self.vtimer.stop()
            self.capture.release()
            #self.labelScreen.setStyleSheet("background-color: black")
            self.labelScreen.clear()
            self.liveStat = False
            self.btnLive.setText("LIVE")
            self.checkPredict.setEnabled(False)
            self.btnPredict.setEnabled(False)

    def liveCam(self):
        self.liveStat = True
        self.btnLive.setText("STOP LIVE")
        self.checkPredict.setEnabled(True)
        self.btnPredict.setEnabled(True)
        cameraName = "0"
        if len(cameraName) == 1:
        	self.capture = cv2.VideoCapture(int(cameraName))
        else:
        	self.capture = cv2.VideoCapture(cameraName)
        self.vtimer = QTimer(self)
        self.vtimer.timeout.connect(self.updateFrame)
        self.vtimer.start(40)

    def updateFrame(self):
        ret, self.image = self.capture.read()
        if self.checkPredict.isChecked() == True:
            self.tampilGambar(self.image, True)
        else:
            self.tampilGambar(self.image, False)

    def loadImage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.tampilGambar(self.image, True)

    def tampilGambar(self, original, pred):
        gambar = cv2.resize(original, (400, 400))
        qformat = QImage.Format_Indexed8
        if len(gambar.shape) == 3:
            if gambar.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(gambar, gambar.shape[1], gambar.shape[0], gambar.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        self.labelScreen.setPixmap(QPixmap.fromImage(outImage))
        self.labelScreen.setScaledContents(True)
        if pred:
            thasil = self.prediksi(original)
            self.labelMaterial.setText(thasil)
        
            

    def prediksi(self,gambar):
        img = cv2.resize(gambar, (400,400))
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, bw) = cv2.threshold(grayImage, 160, 255, cv2.THRESH_BINARY)
        bw = cv2.cvtColor(bw, cv2.COLOR_BGR2RGB)
        x = image.img_to_array(bw)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        labels = ['Type A', 'Type B']
        classes = self.model.predict(images, batch_size=10)
        pred = int(np.argmax(classes, axis=1))
        hasil = labels[pred]
        print(hasil)
        return hasil

    def singleImage(self):
        #self.vtimer.stop()
        self.stopLive()
        self.tampilGambar(self.image, True)


    def checkstate(self):
        if self.checkPredict.isChecked() == True:
            self.btnPredict.setEnabled(False)
        else:
            self.btnPredict.setEnabled(True)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    ui.show()
    sys.exit(app.exec_())
