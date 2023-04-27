import time
import rtmidi
from rtmidi.midiutil import open_midiinput
# from rtmidi.midiconstants import NOTE_ON, NOTE_OFF, TIME_SIGNATURE, TEMPO, END_OF_TRACK
import serial
import serialConnection
# import RPi.GPIO as GPIO
# import spidev
# from lib_nrf24 import NRF24

# establish USB connection with microcontroller
ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
ser.flush()

#
intr = rtmidi.MidiIn()
ports = intr.get_ports()
# print(ports)
intr.open_port(1)

while True:
    if ser.is_open:
        try:
            msgde = intr.get_message()

            if msgde:
                (msg, dt) = msgde
                command = hex(msg[0])
                notestat = msg[0]
                notes = msg[1]
                velocity = msg[2]

                if command == '0x90':
                    # texterON = 'Motor ' + str(motorNO) + ' on\n'
                    texterON = serialConnection.getMotorNo(msg.note) + ',' + 'on' + ',' + '' + '\n'
                    print(texterON + 'is sent')
                    ser.write(texterON.encode('ascii'))
                    #print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")
                elif command == '0x80':
                    # texterOFF = 'Motor ' + str(motorNO) + ' off\n'
                    texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off' + ',' + '' + '\n'
                    print(texterOFF + 'is sent')
                    ser.write(texterOFF.encode('ascii'))
                    #print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")
                elif command == '0x90' and velocity == 0:
                    # texterOFF = 'Motor ' + str(motorNO) + ' off\n'
                    texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off' + ',' + '' + '\n'
                    print(texterOFF + 'is sent')
                    ser.write(texterOFF.encode('ascii'))
                    #print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")            
            else: 
                time.sleep(0.001)
        except:
            ser.close()
    else:
        try:
            ser = serial.Serial('/dev/ttyUSB0',31250, timeout=1)
            ser.flush()
        except:
            pass
    
    time.sleep(1)

