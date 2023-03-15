from mido import MidiFile
from mido import Message
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
ser.flush()

directo = '/home/milo17/Documents/angklungrobot/midi_files/'
mid = MidiFile(directo + 'scale_c_major.mid')
            
def main():
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
        for msg in track:
            #ignores metadata
            if not msg.is_meta:
                note_num = msg.note

                # get motor ref number
                if note_num < 48:
                    pass
                else:
                    if note_num >= 72:
                        motorNO = ((note_num % 12) + 24) + 1
                    elif note_num >= 60:
                        motorNO = ((note_num % 12) + 12) + 1
                    else:
                        motorNO = (note_num % 12)  + 1
                        
                    #if note_on, then display output
                    if msg.type == 'note_on':
                        texterON = 'Motor ' + str(motorNO) + ' on\n'
                        print(texterON + 'is sent')
                        ser.write(texterON.encode('ascii'))
                    elif msg.type == 'note off':
                        texterOFF = 'Motor ' + str(motorNO) + ' off\n'
                        print(texterOFF + 'is sent')
                        ser.write(texterOFF.encode('ascii'))

                    # sleep(dt)

