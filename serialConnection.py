import serial
from serial.tools import list_ports

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
       

# print(getUSBPortName())

# import serial
# from time import sleep
# from RF24 import *

# # Define the radio pinout
# CE_PIN = 22
# CSN_PIN = 0

# # Define the available radio channels and payloads
# num_channels = 2
# num_payloads = 1
# addresses = [0xF0F0F0F0E1, 0xF0F0F0F0E2]
# payload_sizes = [32]

# # Define the RF24 radio object
# radio = RF24(CE_PIN, CSN_PIN)
# radio.begin()
# radio.setPALevel(RF24_PA_MIN)
# radio.setChannel(0)
# radio.setDataRate(RF24_250KBPS)
# radio.setRetries(15, 15)
# radio.setAutoAck(1)
# radio.enableDynamicPayloads()
# radio.openWritingPipe(addresses[1])
# radio.stopListening()

# # Define the USB serial connection
# usb_serial = serial.Serial('/dev/ttyUSB0', 9600)

# # Define the RF serial connection
# rf_serial = serial.Serial('/dev/ttyAMA0', 9600)

# while True:
#     # Send data via USB serial
#     usb_data = input("Enter data to send over USB serial: ")
#     usb_serial.write(usb_data.encode())

#     # Send data via RF
#     rf_data = input("Enter data to send over RF: ")
#     radio.write(rf_data.encode('utf-8'))

#     # Send data via RF serial
#     rf_serial_data = input("Enter data to send over RF serial: ")
#     rf_serial.write(rf_serial_data.encode())

#     # Delay for a short period of time
#     sleep(0.01)


