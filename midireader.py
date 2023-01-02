from mido import MidiFile
from mido import Message

directo = '/home/milo17/Documents/angklungrobot/midi_files/'
mid = MidiFile(directo + 'scale_c_major.mid')

for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
        #print(msg.note)
  
