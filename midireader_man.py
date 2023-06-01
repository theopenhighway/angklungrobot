import time
import rtmidi
from rtmidi.midiutil import open_midiinput
import serial
import serialConnection

def midiManual():
    # establish USB connection with microcontroller
    ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
    ser.flush()

    global condition

    intr = rtmidi.MidiIn()
    ports = intr.get_ports()

    intr.open_port(1)

    condition = True

    while condition == True:
        msgde = intr.get_message()

        if msgde:
            (msg, dt) = msgde
            command = hex(msg[0])
            notestat = msg[0]
            notes = msg[1]
            velocity = msg[2]

            if command == '0x90':
                texterON = serialConnection.getMotorNo(msg.note) + ',' + 'on' + '\n'
                print(texterON + 'is sent')
                ser.write(texterON.encode('ascii'))
            elif command == '0x80':
                texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))
            elif command == '0x90' and velocity == 0:
                texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))           
        else: 
            time.sleep(0.001)
        # QThread.msleep(100)
