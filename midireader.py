from mido import MidiFile
import mido
from time import sleep
import os
import serial
import serialConnection


# ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
ser = serial.Serial('COM4',31250,timeout=1)
ser.flush()

directo = 'C:\\Users\\milo\\personal projects\\angklungrobot\\midi_files\\'
songTitle = 'twinkle-twinkle-little-star.mid'
mid = MidiFile(directo + songTitle)


# print(mid.length)
ticksPerBeat = mid.ticks_per_beat    
dt = 0      
# print(ticksPerBeat)


sleep(2)

for i, track in enumerate(mid.tracks):
    # print('Track {}: {}'.format(i, track.name))
    for msg in track:

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
                dt = (mido.tick2second(msg.time, ticksPerBeat, tempo))
                # intDT = str(int(dt))
                
                if msg.type == 'note_on' and msg.velocity > 0:
                    texterON = serialConnection.getMotorNo(msg.note) + ',' + 'on' + '\n'
                    print(texterON)
                    ser.write(texterON.encode('ascii'))
                    
                elif msg.type == 'note_on' and msg.velocity == 0:
                    texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off' +  '\n'
                    print(texterOFF)
                    ser.write(texterOFF.encode('ascii'))

                elif msg.type == 'note_off':
                    texterOFF = serialConnection.getMotorNo(msg.note) + ',' + 'off' + '\n'
                    print(texterOFF)
                    ser.write(texterOFF.encode('ascii'))
                
                sleep(dt)
                
                
            

# ser.close()