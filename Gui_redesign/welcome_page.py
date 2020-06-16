from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(939, 594)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui_redesign/src/images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("OnkoDicom/logo.ico"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.gridLayout_2.addWidget(self.logo, 4, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.continueButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continueButton.sizePolicy().hasHeightForWidth())

        self.continueButton.setSizePolicy(sizePolicy)
        self.continueButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.continueButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.continueButton.setAutoDefault(True)
        self.continueButton.setDefault(False)
        self.continueButton.setFlat(False)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setStyleSheet("background-color: #9370DB;" "border-width: 8px;" "border-radius: 20px;" "padding: 6px;" "color:white;") # Self added
        self.gridLayout.addWidget(self.continueButton, 2, 0, 1, 1, QtCore.Qt.AlignHCenter) # Keeps button in middle

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(210, -50, 501, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Gui_redesign/src/images/image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.welcome = QtWidgets.QLabel(self.frame_2)
        self.welcome.setGeometry(QtCore.QRect(200, 350, 508, 106))
        self.welcome.setTextFormat(QtCore.Qt.AutoText)
        self.welcome.setScaledContents(False)
        self.welcome.setObjectName("welcome")

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setSizeGripEnabled(False) # Remove expanding window option
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OnkoDICOM"))
        self.continueButton.setText(_translate("MainWindow", "  Open Patient  "))
        self.welcome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Welcome to OnkoDICOM!</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:9pt;\">OnkoDICOM - the solution for producing data for analysis from your oncology plans and scans</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
