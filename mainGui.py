from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
from maxChangeCalculator import calculateMaxChange

def empty(a):
    pass

cv2.namedWindow("Settings")
cv2.createTrackbar("Threshold1", "Settings", 229, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 199, 255, empty)

def preProcessing(img):

    imgPre = cv2.GaussianBlur(img, (5,5), 3)

    # Uncomment to recalibrate thresholds
    thresh1 = cv2.getTrackbarPos("Threshold1", "Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre = cv2.Canny(imgPre, thresh1, thresh2)
    kernel = np.ones((3,3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)

    return imgPre


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 660)
        MainWindow.setStyleSheet("color: rgb(66, 66, 66);\n"
"background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 100, 640, 480))
        self.label.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 44, 44);")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(864, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.disconnectVideo)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(784, 180, 191, 91))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(774, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(890, 290, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(754, 410, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.beginCalculation)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(950, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(754, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.resetCalculator)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(780, 340, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(910, 340, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: green; background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.doubleSpinBox.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.lcdNumber.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.VideoThread = VideoThread()
        self.VideoThread.start()
        self.VideoThread.ImageUpdate.connect(self.ImageUpdateSlot)
        self.VideoThread.ValueUpdate.connect(self.valueUpdateSlot)
        self.VideoThread.sufficient.connect(self.updateSufficientSlot)
        self.doubleSpinBox.valueChanged.connect(self.updateCost)
    

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateSufficientSlot(self, sufficient):
        if sufficient: 
            self.label_7.setText("Sufficient")
            self.label_7.setStyleSheet(f'color: green; background-color: white;')
        else:
            self.label_7.setText("Insufficient")
            self.label_7.setStyleSheet(f'color: red; background-color: white;')

    def updateCost(self, cost):
        self.VideoThread.cost = cost

    def ImageUpdateSlot(self, Image):
        self.label.setPixmap(QPixmap.fromImage(Image))
    
    def valueUpdateSlot(self, value):
        self.lcdNumber.display(value)

    def beginCalculation(self):
        self.VideoThread.switchToCalculate(self.doubleSpinBox.value())
    
    def disconnectVideo(self):
        self.VideoThread.stop()
    
    def resetCalculator(self):
        self.VideoThread.reset()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Loading Video..."))
        self.pushButton.setText(_translate("MainWindow", "Disconnect Video"))
        self.label_2.setText(_translate("MainWindow", "Total Change Value ($)"))
        self.label_3.setText(_translate("MainWindow", "Cost of Item:"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Minimum Change"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Minimum Change Calculator</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "By: Nicholas Chang"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Payment Amount:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Sufficient"))


class VideoThread(QThread):
    ImageUpdate = pyqtSignal(QImage)
    ValueUpdate = pyqtSignal(float)
    sufficient = pyqtSignal(bool)

    isInSumMode = True
    wantToReset = False

    cost = 0

    def run(self):
        self.ThreadActive = True
        cap = cv2.VideoCapture(0)
       
        while self.ThreadActive:
            totalMoney = 0
            coins = []
            self.wantToReset = False
            while self.ThreadActive and self.isInSumMode:
                totalMoney = 0
                coins = []
                success, img = cap.read()
                imgPre = preProcessing(img)
                contours, hiearchy = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cv2.drawContours(img, contours, -1, (0,255,0), 2)

                # dime: ~2000-2500, nickel: ~2900-3300, quarter 3600-4100, loonie: 4250-4950, toonie: 4950-5700

                if contours:
                    for contour in contours:
                        coinArea = cv2.contourArea(contour)
                        # print(coinArea)
                        if coinArea < 2500 and coinArea > 2000:
                            totalMoney += 0.10
                            coins.append(0.10)
                        elif coinArea < 3300 and coinArea > 2900:
                            totalMoney += 0.05
                            coins.append(0.05)
                        elif coinArea < 4100 and coinArea > 3600:
                            totalMoney += 0.25
                            coins.append(0.25)
                        elif coinArea < 4950 and coinArea > 4250:
                            totalMoney += 1.00
                            coins.append(1.00)
                        elif coinArea < 5700 and coinArea >= 4950:
                            totalMoney += 2.00
                            coins.append(2.00)

                    self.ValueUpdate.emit(totalMoney)

                    if totalMoney > self.cost or abs(self.cost - totalMoney) < 0.00001:
                        self.sufficient.emit(True)
                    else:
                        self.sufficient.emit(False)

                    convertToQtFormat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                    pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(pic)
                    cv2.waitKey(1)

            minChange = calculateMaxChange(coins, self.cost)
            print("Min change: " + str(minChange))
            selectedCoins = []

            while self.ThreadActive and not self.wantToReset:
                self.ValueUpdate.emit(totalMoney)
                success, img = cap.read()
                imgPre = preProcessing(img)
                contours, hiearchy = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                if contours:
                    for contour in contours:

                        if len(minChange) == 0:
                            break

                        currentCoin = 0
                        coinArea = cv2.contourArea(contour)
                        if coinArea < 2500 and coinArea > 2000:
                            currentCoin = 0.1
                        elif coinArea < 3300 and coinArea > 2900:
                            currentCoin = 0.05
                        elif coinArea < 4100 and coinArea > 3600:
                            currentCoin = 0.25
                        elif coinArea < 4950 and coinArea > 4250:
                            currentCoin = 1
                        elif coinArea < 5700 and coinArea >= 4950:
                            currentCoin = 2

                        for coin in minChange:
                            if coin == currentCoin:
                                selectedCoins.append(contour)
                                minChange.remove(coin)
                                break

                cv2.drawContours(img, selectedCoins, -1, (255,0,0), 2)
                convertToQtFormat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(pic)
                cv2.waitKey(1)
    
    def recieveCurrentCost(self, cost):
        self.cost = cost

    def switchToCalculate(self, cost):
        self.isInSumMode = False
        self.cost = cost

    def reset(self):
        self.wantToReset = True
        self.isInSumMode = True
        
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
