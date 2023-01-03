from mido import MidiFile
from mido import Message

directo = '/home/milo17/Documents/angklungrobot/midi_files/'
mid = MidiFile(directo + 'scale_c_major.mid')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        #ignore metadata
        if not msg.is_meta:
            note_num = msg.note
            if msg.type == 'note_on':
                #print(msg.note)
                match note_num:
                    case 48:
                        print('C3 on')
                    case 49:
                        print('C#3 on')
                    case 50:
                        print('D3 on')
                    case 51:
                        print('D#3 on')
                    case 52:
                        print('E3 on')
                    case 53:
                        print('F3 on')
                    case 54:
                        print('F#3 on')
                    case 55:
                        print('G3 on')
                    case 56:
                        print('G#3 on')
                    case 57:
                        print('A3 on')
                    case 58:
                        print('A#3 on')
                    case 59:
                        print('B3 on')
                    case 60:
                        print('C4 on')
                    case 61:
                        print('C#4 on')
                    case 62:
                        print('D4 on')
                    case 63:
                        print('D#4 on')
                    case 64:
                        print('E4 on')
                    case 65:
                        print('F4 on')
                    case 66:
                        print('F#4 on')
                    case 67:
                        print('G4 on')
                    case 68:
                        print('G#4 on')
                    case 69:
                        print('A4 on')
                    case 70:
                        print('A#4 on')
                    case 71:
                        print('B4 on')
                    case 72:
                        print('C5 on')
            elif msg.type == 'note_off':
                #print(msg.note)
                match note_num:
                    case 48:
                        print('C3 off')
                    case 49:
                        print('C#3 off')
                    case 50:
                        print('D3 off')
                    case 51:
                        print('D#3 off')
                    case 52:
                        print('E3 off')
                    case 53:
                        print('F3 off')
                    case 54:
                        print('F#3 off')
                    case 55:
                        print('G3 off')
                    case 56:
                        print('G#3 off')
                    case 57:
                        print('A3 off')
                    case 58:
                        print('A#3 off')
                    case 59:
                        print('B3 off')
                    case 60:
                        print('C4 off')
                    case 61:
                        print('C#4 off')
                    case 62:
                        print('D4 off')
                    case 63:
                        print('D#4 off')
                    case 64:
                        print('E4 off')
                    case 65:
                        print('F4 off')
                    case 66:
                        print('F#4 off')
                    case 67:
                        print('G4 off')
                    case 68:
                        print('G#4 off')
                    case 69:
                        print('A4 off')
                    case 70:
                        print('A#4 off')
                    case 71:
                        print('B4 off')
                    case 72:
                        print('C5 off')

        
  
