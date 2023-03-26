from mido import MidiFile
import mido
from time import sleep
import serial
# import pyaudio

# ser = serial.Serial('/dev/ttyUSB0',9600, timeout=1)
# ser.flush()

directo = 'C:\\Users\\milo\\personal projects\\angklungrobot\\midi_files\\'
mid = MidiFile(directo + 'twinkle-twinkle-little-star.mid')

# print(mid.length)
ticksPerBeat = mid.ticks_per_beat   
tempo = 0         
# print(ticksPerBeat)

# get motor ref number
def getMotorNo(note_num):
    if note_num >= 72:
        return str(((note_num % 12) + 24) + 1)
    elif note_num >= 60:
        return str(((note_num % 12) + 12) + 1)
    else:
        return str((note_num % 12)  + 1)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        # tempo = getTempo(mid)
        # print(msg.time)

        if msg.is_meta and msg.type == 'set_tempo':
            # tempo: microsecond per quarter note
            # default tempo: 120 BPM (500000 microsecond per quarter note)
            # default time signature: 4/4
            tempo = msg.tempo
            
        elif not msg.is_meta and (msg.type != 'control_change' and msg.type != 'program_change' and msg.type != 'aftertouch' and msg.type != 'pitchwheel' and msg.type != 'sysex'):

            # skip if note number is not within the required range
            if msg.note < 48 and msg.note > 72:
                pass
            
            else:
                if msg.type == 'note_on':
                    texterON = 'Motor ' + getMotorNo(msg.note) + ' on\n'
                    # print(texterON + 'is sent')
                    # ser.write(texterON.encode('ascii'))
                    print(texterON)

                elif msg.type == 'note_off':
                    texterOFF = 'Motor ' + getMotorNo(msg.note) + ' off\n'
                    # print(texterOFF + 'is sent')
                    # ser.write(texterOFF.encode('ascii'))
                    print(texterOFF)
                
                dt = mido.tick2second(msg.time, ticksPerBeat, tempo)
                sleep(dt)

