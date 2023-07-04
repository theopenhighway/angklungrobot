from mido import MidiFile
import mido
from time import sleep
import serial
import rtmidi
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from serial.tools import list_ports

def serialDisconnect():
    pass

def controllerDisconnect():
    pass

# find USB port address
def getUSBPortName():
    enmu_ports = enumerate(list_ports.comports())
    port = ""
        
    for n, (p, descriptor, hid) in enmu_ports:
        # print(p,descriptor, hid)
        # print(descriptor)
        if "USB-SERIAL CH340 (COM4)" or "Standard Serial over Bluetooth link (COM8)" in descriptor:
            port = p.split()
            return str(port[0])

#converts note number to motor no (e.g. C3 - 48 = Motor 1)
def getMotorNo(note_num):
    if note_num >= 72:
        return str(((note_num % 12) + 24) + 1)
    elif note_num >= 60:
        return str(((note_num % 12) + 12) + 1)
    else:
        return str((note_num % 12)  + 1)

def check_serial_connection(self):
    if self.serial is None or not self.serial.is_open:
        try:
            self.serial = serial.Serial('COM3', 9600)  # Replace 'COM3' with your microcontroller's port
            self.label.setText("Connected")
        except serial.SerialException:
            self.serial = None
            self.label.setText("Disconnected")

def midiOtomatis(songTitleX, thread, self):
    # ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
    # ser = serial.Serial('COM3',31250,timeout=1)

    #linux ver
    # ser = serial.Serial('/dev/ttyACM0',31250,timeout=1)
    # directo = 'midi_files//'

    # windows ver
    ser = serial.Serial('COM5',31250,timeout=1)
    directo = 'midi_files\\'
    
    ser.flush()

    
    #songTitle = 'twinkle-twinkle-little-star.mid'
    songTitle = songTitleX
    mid = MidiFile(directo + songTitle)


    ticksPerBeat = mid.ticks_per_beat    
    dt = 0      
    tempo = 0

    def setTempo(msg):
        if msg.tempo == None:
            return 500000
        else:
            return msg.tempo

    sleep(2)



    for msg in mid:
        sleep(msg.time)

        if not msg.is_meta and (msg.type != 'control_change' and msg.type != 'program_change' and msg.type != 'aftertouch' and msg.type != 'pitchwheel' and msg.type != 'sysex'):
            if msg.type == 'note_on' and msg.velocity > 0:
                texterON =  getMotorNo(msg.note) + ',' + 'on' + '\n'
                print(texterON) 
                ser.write(texterON.encode('ascii'))
                    
            elif msg.type == 'note_on' and msg.velocity == 0:
                texterOFF =  getMotorNo(msg.note) + ',' + 'off' + '\n'
                print(texterOFF)
                ser.write(texterOFF.encode('ascii'))

            elif msg.type == 'note_off':
                texterOFF =  getMotorNo(msg.note) + ',' + 'off' + '\n'
                print(texterOFF)
                ser.write(texterOFF.encode('ascii'))
                

        if thread.is_paused():
            while thread.is_paused():
                QThread.msleep(100)  # Sleep to reduce CPU usage while paused

        if thread.isInterruptionRequested():
            return
          
def midiManual(thread):

    #linux ver
    # ser = serial.Serial('/dev/ttyACM0',31250,timeout=1)

    # windows ver
    ser = serial.Serial('COM5',31250,timeout=1)
    ser.flush()

    intr = rtmidi.MidiIn()
    ports = intr.get_ports()

    intr.open_port(0)

    while thread.condition:
        msgde = intr.get_message()

        if msgde:
            (msg, dt) = msgde
            command = hex(msg[0])
            notestat = msg[0]
            notes = msg[1]
            velocity = msg[2]

            if command == '0x90':
                texterON = getMotorNo(notes) + ',' + 'on' + '\n'
                print(texterON + 'is sent')
                ser.write(texterON.encode('ascii'))
            elif command == '0x80':
                texterOFF = getMotorNo(notes) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))
            elif command == '0x90' and velocity == 0:
                texterOFF = getMotorNo(notes) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))
        else:
            sleep(0.001)
        
        # thread.serial = None
        # thread.timer = QTimer()
        # thread.timer.timeout.connect(self.check_serial_connection)
        # thread.timer.start(1000)  

    # ser.close()