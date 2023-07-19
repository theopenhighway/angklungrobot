from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox, QWidget, QAction
from PyQt5.QtCore import QThread, pyqtSignal, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
import midireader
from time import sleep
import serial.tools.list_ports

# assets
HEIGHT = 720
WIDTH = 1280
SETTINGS_ICON = 'gui_asset\\settings.png'

serialPort = midireader.portName


class stockImages:
    def loadImage(imagePath):
        pixMap = QPixmap(imagePath)
        return QIcon(pixMap)

# code to run midi manual
class MidiManualThread(QThread):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.condition = True

    def run(self):
        midireader.midiManual(self)

    def stop(self):
        self.condition = False

# code to run midi otomatis
class MidiPlayerThread(QThread):
    finished = pyqtSignal()

    def __init__(self, song_title):
        super().__init__()
        self.song_title = song_title
        self.paused = False

    def run(self):
        midireader.midiOtomatis(self.song_title, self)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def is_paused(self):
        return self.paused
    
    def stop(self):
        self.stop_midi

# main menu page
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        MainWindow.setWindowTitle("Stop Function Example")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # settings button
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setIcon(stockImages.loadImage(SETTINGS_ICON)) 
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
        
        self.otomatisText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.otomatisText.setFont(font)
        self.otomatisText.setObjectName("otomatisText")
        self.horizontalLayout_3.addWidget(self.otomatisText)
        
        self.manualText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualText.sizePolicy().hasHeightForWidth())
        self.manualText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.manualText.setFont(font)
        self.manualText.setTabletTracking(False)
        self.manualText.setObjectName("manualText")
        self.horizontalLayout_3.addWidget(self.manualText)
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
        
        # settings menu
        self.context_menu = QMenu(MainWindow)
        settingsAction = QAction("Settings", MainWindow)
        documentationAction = QAction("Documentation", MainWindow)
        aboutAction = QAction("About", MainWindow)

        self.context_menu.addAction(settingsAction)
        self.context_menu.addAction(documentationAction)
        self.context_menu.addAction(aboutAction)

        settingsAction.triggered.connect(universalFunction.handleSettingsAction)
        documentationAction.triggered.connect(universalFunction.handleDocsAction)
        aboutAction.triggered.connect(universalFunction.handleAboutAction)
        self.webView = None
        self.toolButton.setMenu(self.context_menu)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)

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

        self.modeOtomatis.showMaximized()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "angklungrobot"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.welcomeText.setText(_translate("MainWindow", "WELCOME"))
        self.instructionText.setText(_translate("MainWindow", "Select the desired mode."))
        self.modeOtomatis.setText(_translate("MainWindow", "Automatic Mode"))
        self.modeManual.setText(_translate("MainWindow", "Manual Mode"))
        self.manualText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Play the keyboard to interact.</p></body></html>"))
        self.otomatisText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"> Let this angklung play on its own. </p></body></html>"))

# mode manual page
class Ui_modeManual(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle('AngklungRobot')
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
        self.backButton.clicked.connect(self.backToMainMenu)

        # settings button
        self.settingsButton = QtWidgets.QToolButton(self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setIcon(stockImages.loadImage(SETTINGS_ICON)) 
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

        self.midi_player_thread = None
        self.start_midi()

        # settings menu
        self.context_menu = QMenu(MainWindow)
        settingsAction = QAction("Settings", MainWindow)
        documentationAction = QAction("Documentation", MainWindow)
        aboutAction = QAction("About", MainWindow)

        self.context_menu.addAction(settingsAction)
        self.context_menu.addAction(documentationAction)
        self.context_menu.addAction(aboutAction)

        settingsAction.triggered.connect(universalFunction.handleSettingsAction)
        documentationAction.triggered.connect(universalFunction.handleDocsAction)
        aboutAction.triggered.connect(universalFunction.handleAboutAction)
    
        self.webView = None
        self.settingsButton.setMenu(self.context_menu)
        self.settingsButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)


    def start_midi(self):
        self.midi_player_thread = MidiManualThread()
        self.midi_player_thread.finished.connect(self.on_midi_finished)
        self.midi_player_thread.start()

    # return to main menu
    def backToMainMenu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainMenu)
        self.mainMenu.showMaximized()
        MainWindow.close()

        if self.midi_player_thread:
            self.midi_player_thread.stop()
            self.midi_player_thread.terminate()
            self.midi_player_thread = None
            print('player stopped')

    def on_midi_finished(self):
        self.midi_player_thread = None
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.settingsButton.setText(_translate("MainWindow", "..."))
        self.modeManualTitle.setText(_translate("MainWindow", "MANUAL MODE"))
        self.manualInst.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Silahkan tekan tuts keyboard yang disediakan untuk <br/>berinteraksi langsung dengan angklung ini!</span></p></body></html>"))

# mode otomatis page
class Ui_modeOtomatis(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("AngklungRobot")
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
        
        # back to menu button
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setObjectName("backButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.backButton)
        self.backButton.clicked.connect(self.backToMainMenu)

        # settings menu
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setIcon(stockImages.loadImage(SETTINGS_ICON)) 
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        
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
        
        # list widget
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

        # pause button
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setObjectName("pauseButton")
        self.verticalLayout.addWidget(self.pauseButton)

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
        dir_path = "midi_files\\"
        
        for file in os.listdir(dir_path):
            
            if os.path.isfile(os.path.join(dir_path, file)):
                self.listWidget.addItem(QtWidgets.QListWidgetItem(file))
        

        # scroll bar for list widget
        scroll_area = QtWidgets.QScrollArea(self.centralwidget)  # Create a scroll area with central widget as parent
        scroll_area.setWidgetResizable(True)  # Allow the widget to resize with the scroll area
        scroll_area.setWidget(self.listWidget)  # Set the list widget as the scroll area's widget

        self.verticalLayout.addWidget(scroll_area)  # Add the scroll area to the layout
        MainWindow.setCentralWidget(self.centralwidget)  
        
        # set value when user presses list widget
        self.listWidget.itemClicked.connect(self.on_item_clicked)
        
        # add command for play button
        self.playButton.clicked.connect(self.run_midi)

        # pause midi 
        self.pauseButton.clicked.connect(self.pause_midi)
        self.pauseButton.setEnabled(False)

        # stop midi
        self.stopButton.clicked.connect(self.stop_midi)
        self.stopButton.setEnabled(False)

        # context menu when toolbar is pressed
        self.context_menu = QMenu(MainWindow)
        settingsAction = QAction("Settings", MainWindow)
        documentationAction = QAction("Documentation", MainWindow)
        aboutAction = QAction("About", MainWindow)

        self.context_menu.addAction(settingsAction)
        self.context_menu.addAction(documentationAction)
        self.context_menu.addAction(aboutAction)

        settingsAction.triggered.connect(universalFunction.handleSettingsAction)
        documentationAction.triggered.connect(universalFunction.handleDocsAction)
        aboutAction.triggered.connect(universalFunction.handleAboutAction)

        self.webView = None
        self.toolButton.setMenu(self.context_menu)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)

    def on_item_clicked(self, item):
        self.selected_item = item.text()
        return self.selected_item
       
    def run_midi(self):
        song_title = self.selected_item  # Replace 'your_song_title.mid' with the actual song title
        self.midi_player_thread = MidiPlayerThread(song_title)
        self.midi_player_thread.finished.connect(self.on_midi_finished)
        self.midi_player_thread.start()
        self.playButton.setEnabled(False)
        self.pauseButton.setEnabled(True)
        self.stopButton.setEnabled(True)

    def pause_midi(self):
        if self.midi_player_thread and not self.midi_player_thread.is_paused():
            self.midi_player_thread.pause()
            self.pauseButton.setText('Resume')
            print('player paused')
        elif self.midi_player_thread:
            self.midi_player_thread.resume()
            self.pauseButton.setText('Pause')
            print('player resumed')

    def stop_midi(self):
        if self.midi_player_thread:
            self.midi_player_thread.terminate()
            self.midi_player_thread = None
        self.playButton.setEnabled(True)
        self.pauseButton.setEnabled(False) 
        self.pauseButton.setText('Pause')
        self.stopButton.setEnabled(False)
        print('player stopped')

    def on_midi_finished(self):
        self.midi_player_thread = None
        self.playButton.setEnabled(True)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setText('Pause')
        self.stopButton.setEnabled(False)

    def hideMidiOtomatis(self):
        self.modeOtomatis = QtWidgets.QMainWindow()
        self.ui = Ui_modeOtomatis()
        self.ui.setupUi(self.modeOtomatis)
        self.modeOtomatis.hide()

    # return to main menu
    def backToMainMenu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainMenu)
        self.mainMenu.showMaximized()
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.modeOtomatisTitle.setText(_translate("MainWindow", "AUTOMATIC MODE"))
        self.label.setText(_translate("MainWindow", "Song List"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

        self.closeButton.clicked.connect(self.close)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(396, 265)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleName = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleName.setFont(font)
        self.titleName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleName.setObjectName("titleName")
        self.verticalLayout.addWidget(self.titleName, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serialText = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.serialText.setFont(font)
        self.serialText.setObjectName("serialText")
        self.horizontalLayout.addWidget(self.serialText)
        self.statusSerial = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusSerial.setFont(font)
        self.statusSerial.setObjectName("statusSerial")
        self.horizontalLayout.addWidget(self.statusSerial)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout.addLayout(self.horizontalLayout_8)
        self.reconnectSerial = QtWidgets.QPushButton(self)
        self.reconnectSerial.setObjectName("reconnectSerial")
        self.horizontalLayout.addWidget(self.reconnectSerial)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.MIDItext = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MIDItext.setFont(font)
        self.MIDItext.setObjectName("MIDItext")
        self.horizontalLayout_5.addWidget(self.MIDItext)
        self.statusMIDI = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusMIDI.setFont(font)
        self.statusMIDI.setObjectName("statusMIDI")
        self.horizontalLayout_5.addWidget(self.statusMIDI)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)
        self.reconnectMIDI = QtWidgets.QPushButton(self)
        self.reconnectMIDI.setObjectName("reconnectMIDI")
        self.horizontalLayout_5.addWidget(self.reconnectMIDI)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.closeButton = QtWidgets.QPushButton(self)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_7.addWidget(self.closeButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        
        try:
            ser = serial.Serial(serialPort)
            if ser.is_open:
                self.reconnectSerial.setEnabled(False)
                self.statusSerial.setText('Connected')
                ffe = False
            else:
                self.reconnectSerial.setEnabled(True)
                self.statusSerial.setText('Disconnected')
                print(f"Serial port {serialPort} is already closed")
        except serial.SerialException as e:
                self.reconnectSerial.setEnabled(True)
                self.statusSerial.setText('Disconnected')
                print(f"{serialPort}: {e}")
        
        sleep(0.01)
        
    def reconnectSerial(self):
        ser = serialPort

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleName.setText(_translate("Dialog", "Connection Status"))
        self.serialText.setText(_translate("Dialog", "Microcontroller: "))
        self.statusSerial.setText(_translate("Dialog", " Connected"))
        self.reconnectSerial.setText(_translate("Dialog", "Reconnect"))
        self.MIDItext.setText(_translate("Dialog", "MIDI Controller: "))
        self.statusMIDI.setText(_translate("Dialog", " Connected"))
        self.reconnectMIDI.setText(_translate("Dialog", "Reconnect"))
        self.closeButton.setText(_translate("Dialog", "Close"))

class universalFunction:
    # settings object
    def handleSettingsAction(self):
        settings_dialog = SettingsDialog()
        settings_dialog.exec_()
    
    def handleDocsAction(self):
        url = QUrl("https://github.com/theopenhighway") 
        QDesktopServices.openUrl(url)

    def handleAboutAction(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("About")
        msg_box.setText("angklungrobot 2023 <br> version 1.0")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        # print("Action 3 triggered")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
