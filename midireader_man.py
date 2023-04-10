import time
import rtmidi
from rtmidi.midiutil import open_midiinput
# from rtmidi.midiconstants import NOTE_ON, NOTE_OFF, TIME_SIGNATURE, TEMPO, END_OF_TRACK
import serial
# import RPi.GPIO as GPIO
# import spidev
# from lib_nrf24 import NRF24

# establish USB connection with microcontroller
ser = serial.Serial('/dev/ttyUSB0',31250, timeout=1)
ser.flush()

#
intr = rtmidi.MidiIn()
ports = intr.get_ports()
# print(ports)
intr.open_port(1)

while True:
    msgde = intr.get_message()

    if msgde:
        (msg, dt) = msgde
        command = hex(msg[0])
        notestat = msg[0]
        notes = msg[1]
        velocity = msg[2]
        
        # get motor ref numbergpio 
        if notes >= 72:
            motorNO = ((notes % 12) + 24) + 1
        elif notes >= 60:
            motorNO = ((notes % 12) + 12) + 1
        else:
            motorNO = (notes % 12)  + 1

        if command == '0x90':
            texterON = 'Motor ' + str(motorNO) + ' on\n'
            print(texterON + 'is sent')
            ser.write(texterON.encode('ascii'))
            #print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")
        elif command == '0x80':
            texterOFF = 'Motor ' + str(motorNO) + ' off\n'
            print(texterOFF + 'is sent')
            ser.write(texterOFF.encode('ascii'))
            #print(f"{command} {msg[1:]}\t| dt = {dt:.2f}")
    else: 
        time.sleep(0.001)

