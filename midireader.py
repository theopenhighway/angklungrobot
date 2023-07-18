from mido import MidiFile
import mido
from time import sleep
import serial
import rtmidi
from PyQt5.QtCore import QThread
from serial.tools import list_ports


portNameWindows = 'COM3'
portNamwLinux = '/dev/ttyACM0'

def openSerialPort(name):
    ser = serial.Serial(name,31250,timeout=1)
    return ser

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
    if note_num == 72:
        return str(((note_num % 12) + 24) + 1)
    elif note_num >= 60:
        return str(((note_num % 12) + 12) + 1)
    elif note_num >= 48:
        return str((note_num % 12)  + 1)
    else:
        return str(0)


def midiOtomatis(songTitleX, thread):
    # ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
    # ser = serial.Serial('COM3',31250,timeout=1)

    #linux ver
    # ser = serial.Serial(portNameLinux,31250,timeout=1)
    # directo = 'midi_files//'

    # windows ver
    ser = openSerialPort(portNameWindows)
    directo = 'midi_files\\'
    
    ser.flush()
    sleep(2)
    
    #songTitle = 'twinkle-twinkle-little-star.mid'
    songTitle = songTitleX
    mid = MidiFile(directo + songTitle)

    for msg in mid:
        sleep(msg.time)

        if not msg.is_meta:
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
            elif msg.type == 'end_of_track':
                ser.close()

        if thread.is_paused():
            while thread.is_paused():
                QThread.msleep(100)  # Sleep to reduce CPU usage while paused

        if thread.isInterruptionRequested():
            return
    
    ser.close()
          
def midiManual(thread):
    # windows ver
    ser = openSerialPort(portNameWindows)

    #linux ver
    # ser = serial.Serial(portNamwLinux,31250,timeout=1)
    ser.flush()

    intr = rtmidi.MidiIn()
    intr.open_port(0)

    while thread.condition:
        msgde = intr.get_message()

        if msgde:
            (msg, dt) = msgde
            command = hex(msg[0])
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
 
    # ser.close()