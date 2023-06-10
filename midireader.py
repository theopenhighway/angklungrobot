from mido import MidiFile
import mido
from time import sleep
import serial
import serialConnection
import rtmidi
from PyQt5.QtCore import QThread

def midiOtomatis(songTitleX, thread):
    # ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
    ser = serial.Serial('COM3',31250,timeout=1)
    ser.flush()

    directo = 'midi_files\\'
    #songTitle = 'twinkle-twinkle-little-star.mid'
    songTitle = songTitleX
    mid = MidiFile(directo + songTitle)


    # print(mid.length)
    ticksPerBeat = mid.ticks_per_beat    
    dt = 0      
    # print(ticksPerBeat)

    def setTempo(msg):
        if msg.tempo != None:
            return 500000
        else:
            return msg.tempo

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

            if thread.is_paused():
                while thread.is_paused():
                    QThread.msleep(100)  # Sleep to reduce CPU usage while paused

            if thread.isInterruptionRequested():
                return

                    
def midiManual(thread):
    ser = serial.Serial('COM3', 31250, timeout=1)
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
                texterON = serialConnection.getMotorNo(notes) + ',' + 'on' + '\n'
                print(texterON + 'is sent')
                ser.write(texterON.encode('ascii'))
            elif command == '0x80':
                texterOFF = serialConnection.getMotorNo(notes) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))
            elif command == '0x90' and velocity == 0:
                texterOFF = serialConnection.getMotorNo(notes) + ',' + 'off'  + '\n'
                print(texterOFF + 'is sent')
                ser.write(texterOFF.encode('ascii'))
        else:
            sleep(0.001)
        

    # ser.close()