from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox, QWidget, QAction
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import serial
import midireader

HEIGHT = 720
WIDTH = 1280

# main menu page
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        MainWindow.setWindowTitle("Stop Function Example")
        # QMainWindow.setWindowTitle("AngklungRobot")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # settings button
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

    def start_midi(self):
        self.midi_player_thread = MidiManualThread()
        self.midi_player_thread.finished.connect(self.on_midi_finished)
        self.midi_player_thread.start()

    # return to main menu
    def backToMainMenu(self):
        self.mainMenu = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainMenu)
        self.mainMenu.show()
        MainWindow.hide()

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
        self.modeManualTitle.setText(_translate("MainWindow", "MODE MANUAL"))
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
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.toolButton)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton.setMenu(self.show_context_menu)

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
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(self.listWidget)

        # Set the QScrollArea as the central widget of the main window
        self.setCentralWidget(scroll_area)

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
        elif self.midi_player_thread:
            self.midi_player_thread.resume()
            self.pauseButton.setText('Pause')

    def stop_midi(self):
        if self.midi_player_thread:
            self.midi_player_thread.terminate()
            self.midi_player_thread = None
        self.playButton.setEnabled(True)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setText('Pause')
        self.stopButton.setEnabled(False)

    def on_midi_finished(self):
        self.midi_player_thread = None
        self.playButton.setEnabled(True)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setText('Pause')
        self.stopButton.setEnabled(False)

    # context menu when toolbar is pressed
    def show_context_menu(self):
        context_menu = QMenu(self)
        settingsMenu = QAction("Settings", self)
        statusMenu = QAction("Status: ", self)
        helpMenu = QAction("Help", self)

        context_menu.addAction(settingsMenu)
        context_menu.addAction(statusMenu)
        context_menu.addAction(helpMenu)

        settingsMenu.triggered.connect(self.handle_action1)
        statusMenu.triggered.connect(self.handle_action2)
        helpMenu.triggered.connect(self.handle_action3)

        context_menu.exec_(self.button.mapToGlobal(self.button.rect().bottomLeft()))

    def handle_action1(self):
        print("Action 1 triggered")

    def handle_action2(self):
        print("Action 2 triggered")

    def handle_action3(self):
        print("Action 3 triggered")

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
        self.mainMenu.show()
        MainWindow.hide()
        self.hideMidiOtomatis()

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
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
