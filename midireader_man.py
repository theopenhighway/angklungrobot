from mido import MidiFile
import mido
from time import sleep
import serial
import serialConnection
import rtmidi

# base code, not implemented

def midiManual():
    # establish USB connection with microcontroller
    # ser = serial.Serial(serialConnection.getUSBPortName(),31250, timeout=1)
    ser = serial.Serial('COM5',31250, timeout=1)
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
        # QThread.msleep(100)

def midiOtomatis(x):
    # windows ver
    ser = serial.Serial('COM5',31250,timeout=1)
    directo = 'midi_files\\'
    
    ser.flush()
    
    songTitle = x
    directo = 'midi_files//'
    mid = MidiFile(directo + songTitle)
    


    # print(mid.length)
    ticksPerBeat = mid.ticks_per_beat    
    dt = 0      
    tempo = 0
    # print(ticksPerBeat)

    def getMotorNo(note_num):
        if note_num >= 72:
            return str(((note_num % 12) + 24) + 1)
        elif note_num >= 60:
            return str(((note_num % 12) + 12) + 1)
        elif note_num >=48:
            return str((note_num % 12)  + 1)
        else:
            return 0
    
    def setTempo(msg):
        if msg.tempo != None:
            return msg.tempo
        else:
            return 500000
            
    sleep(2)


    for msg in mid:
        dt = (mido.tick2second(msg.time, ticksPerBeat, tempo))
        
        sleep(dt)

        if msg.is_meta and msg.type == 'set_tempo':
            # tempo: microsecond per quarter note
            # default tempo: 120 BPM (500000 microsecond per quarter note)
            # default time signature: 4/4
            tempo = setTempo(msg)
            
        elif not msg.is_meta and (msg.type != 'control_change' and msg.type != 'program_change' and msg.type != 'aftertouch' and msg.type != 'pitchwheel' and msg.type != 'sysex'):
            # skip if note number is not within the required range

            
            if msg.type == 'note_on' and msg.velocity > 0:
                texterON =  getMotorNo(msg.note)  + ',' + 'on' + ',' + '\n'
                print(texterON + str(dt)) 
                ser.write(texterON.encode('ascii'))
                
            elif msg.type == 'note_on' and msg.velocity == 0:
                texterOFF =  getMotorNo(msg.note) + ',' + 'off' + ',' + '\n'
                print(texterOFF + str(dt))
                ser.write(texterOFF.encode('ascii'))

            elif msg.type == 'note_off':
                texterOFF =  getMotorNo(msg.note) + ',' + 'off' + ',' + '\n'
                print(texterOFF)
                ser.write(texterOFF.encode('ascii'))
                    
def printMidiEvent(z):
    songTitle = z
    directo = 'midi_files//'
    def setTempo(msg):
        if msg.tempo == None:
            return 500000
        else:
            return msg.tempo

    mid = MidiFile(directo + songTitle)
    for i, track in enumerate(mid.tracks):
        # print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if msg.is_meta and msg.type == 'set_tempo':
                # tempo: microsecond per quarter note
                # default tempo: 120 BPM (500000 microsecond per quarter note)
                # default time signature: 4/4
                tempo = setTempo(msg)
                print(tempo)
            else:
                print(msg)

def midiPlayback(x):
    def getMotorNo(note_num):
        if note_num >= 72:
            return str(((note_num % 12) + 24) + 1)
        elif note_num >= 60:
            return str(((note_num % 12) + 12) + 1)
        elif note_num >=48:
            return str((note_num % 12)  + 1)
        else:
            return 0
       
    ser = serial.Serial('COM5',31250,timeout=1)
    ser.flush()
    songTitle = x
    directo = 'midi_files//'
    mid = MidiFile(directo + songTitle)

    

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

    ser.close()           

if __name__ == "__main__":
    midiPlayback('Pengujian Chord Mayor.mid')
    # midiOtomatis('Pengujian Chord Mayor.mid')
    #printMidiEvent('Pengujian Chord Mayor.mid')
    