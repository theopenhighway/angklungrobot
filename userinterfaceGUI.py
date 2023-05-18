from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox
from PyQt5.QtGui import QIcon
import serial

HEIGHT = 720
WIDTH = 1280

# main menu page
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.welcomeText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeText.setFont(font)
        self.welcomeText.setObjectName("welcomeText")
        self.verticalLayout_2.addWidget(self.welcomeText, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
       
        self.instructionText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.instructionText.setFont(font)
        self.instructionText.setObjectName("instructionText")
        self.verticalLayout_2.addWidget(self.instructionText, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # mode otomatis button
        self.modeOtomatis = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeOtomatis.sizePolicy().hasHeightForWidth())
        self.modeOtomatis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.modeOtomatis.setFont(font)
        self.modeOtomatis.setObjectName("modeOtomatis")
        self.horizontalLayout_2.addWidget(self.modeOtomatis) 
        self.modeOtomatis.clicked.connect(self.midiOtomatis)

        # mode manual button
        self.modeManual = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeManual.sizePolicy().hasHeightForWidth())
        self.modeManual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.modeManual.setFont(font)
        self.modeManual.setObjectName("modeManual")
        self.horizontalLayout_2.addWidget(self.modeManual)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.modeManual.clicked.connect(self.midiManual)
        
        self.manualText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manualText.setFont(font)
        self.manualText.setObjectName("manualText")
        self.horizontalLayout_3.addWidget(self.manualText)
        
        self.otomatisText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otomatisText.sizePolicy().hasHeightForWidth())
        self.otomatisText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.otomatisText.setFont(font)
        self.otomatisText.setTabletTracking(False)
        self.otomatisText.setObjectName("otomatisText")
        self.horizontalLayout_3.addWidget(self.otomatisText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def midiManual(self):
        self.modeManual = QtWidgets.QMainWindow()
        self.ui = Ui_modeManual()
        self.ui.setupUi(self.modeManual)
        self.modeManual.showMaximized()
        MainWindow.hide()
        
    def midiOtomatis(self):
        self.modeOtomatis = QtWidgets.QMainWindow()
        self.ui = Ui_modeOtomatis()
        self.ui.setupUi(self.modeOtomatis)

        self.modeOtomatis.show()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.welcomeText.setText(_translate("MainWindow", "SELAMAT DATANG"))
        self.instructionText.setText(_translate("MainWindow", "Silahkan pilih mode yang ingin digunakan"))
        self.modeOtomatis.setText(_translate("MainWindow", "Mode Otomatis"))
        self.modeManual.setText(_translate("MainWindow", "Mode Manual"))
        self.manualText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mainkan angklung ini dengan menekan tuts <br/>pada keyboard yang telah disediakan</p></body></html>"))
        self.otomatisText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Ingin melihat angklung ini bermain secara otomatis? <br/>Pilihlah mode ini</p></body></html>"))

# mode manual page
class Ui_modeManual(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        # back button
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.backButton)
        
        # settings button
        self.settingsButton = QtWidgets.QToolButton(self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.settingsButton)
        
        self.verticalLayout_3.addLayout(self.formLayout)
        self.modeManualTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.modeManualTitle.setFont(font)
        self.modeManualTitle.setObjectName("modeManualTitle")
        self.verticalLayout_3.addWidget(self.modeManualTitle, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        
        self.manualInst = QtWidgets.QLabel(self.centralwidget)
        self.manualInst.setObjectName("manualInst")
        self.verticalLayout_3.addWidget(self.manualInst, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def backToMainMenu(self):
        self.modeManual = QtWidgets.QMainWindow()
        self.ui = Ui_modeManual()
        self.ui.setupUi(self.modeManual)
        self.modeManual.showMaximized()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.settingsButton.setText(_translate("MainWindow", "..."))
        self.modeManualTitle.setText(_translate("MainWindow", "MODE MANUAL"))
        self.manualInst.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Silahkan tekan tuts keyboard yang disediakan untuk <br/>berinteraksi langsung dengan angklung ini!</span></p></body></html>"))

# mode otomatis page
class Ui_modeOtomatis(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_3.setObjectName("formLayout_3")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName("backButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.backButton)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.verticalLayout.addLayout(self.formLayout_3)
        
        self.modeOtomatisTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.modeOtomatisTitle.setFont(font)
        self.modeOtomatisTitle.setObjectName("modeOtomatisTitle")
        self.verticalLayout.addWidget(self.modeOtomatisTitle, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
       
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        
        # play button
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_11.addWidget(self.playButton)

        # stop button
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        # self.horizontalLayout_11.addWidget(self.stopButton)
        self.verticalLayout.addWidget(self.stopButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # gets song title based file name to list widget
        import os
        dir_path = "C:\\Users\\milo\\personal projects\\angklungrobot\\midi_files\\"
        
        for file in os.listdir(dir_path):
            
            if os.path.isfile(os.path.join(dir_path, file)):
                self.listWidget.addItem(QtWidgets.QListWidgetItem(file))
        
        # scroll bar for list widget
        # self.scrollBar = QtWidgets.QScrollBar(self.listWidget)
        # self.listWidget.addScrollBarWidget(self.scrollBar, QtCore.Qt.AlignRight)
        # self.listWidget.verticalScrollBar()
        

        # set value when user presses list widget
        # self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.selectionMode())
        # for item in self.listwidget.selectedItems():
            # print(item.text())

    def returnToMainMenu(self):
        print()

    # if serial connection failed, then a pop up menu will show up
    def popUpUSB(self):
        msg = QMessageBox()
        msg.setWindowTitle("Angklung Tidak Terhubung")
        msg.setText("Sambungkan kembali koneksi USB Raspberry Pi dengan mikrokontroller.")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Retry|QMessageBox.Ignore)
        msg.buttonClicked.connect(self.popUpButton)
    
    def popUpButton(self, i):
        if i.text() == 'Retry':
            print()
        elif i.text == 'Xancel':
            print()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.modeOtomatisTitle.setText(_translate("MainWindow", "MODE OTOMATIS"))
        self.label.setText(_translate("MainWindow", "Pilihan Lagu"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
