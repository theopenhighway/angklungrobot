# Angklung Robot

## Overview

This is a repository based on my undergraduate thesis, titled "Perancangan Sistem Otomatisasi Alat Musik Angklung dengan Input Berformat MIDI" (translation: Design of an Automated Angklung Musical Instrument System with MIDI Input). It is a system that allows an angklung (Indonesian traditional musical instrument) to operate automatically based on MIDI events.

There are two modes available on this system:

- Read and parse MIDI file
- Sending MIDI events via MIDI controller

## Requirements

- Python 3.9.2 or higher
- Raspbian OS (or Windows 10 and up is supported with couple of modifications)


## Technical Specification

- Raspberry Pi 4B 4GB
- Arduino Mega 2560
- Relay Module
- N20 Gearbox 1000 RPM DC Motor
- 25-Key MIDI Controller

## Dependencies

Install the following dependencies

RtMidi v1.4.9

``` 
pip install python-rtmidi 
```

Mido v1.2.10
``` 
pip install mido==1.2.10
```

pyQt5 version 5.15.9
``` 
pip install PyQt5 
```

## Repository Organization
| File/Folder Name | Description |
|------|----|
|midireader_man.py |Reads and parses MIDI events from MIDI controller to serial data|
|midireader.py |Reads and parses MIDI events from a MIDI file to serial data|
|userinterfaceGUI.py |The system's GUI|
|sketch_apr5a.ino |Reads serial data from Raspberry Pi to control DC motor|
|gui_asset |fonts and images for userinterfaceGUI.py |
|midi_files |MIDI files file path for midireader.py. All MIDI files has to be placed here |

## Modifications for Windows
| File Name | Code | Modification
|------|----|---|
|userintefaceGUI.py|SETTINGS_ICON = 'gui_asset\\settings.png'| change \\ to /|
|userintefaceGUI.py|dir_path = "midi_files\\"| change \\ to /|
|midireader.py|ser = serial.Serial('dev/ttyAMA0',31250, timeout=1)| change serial name to COMx (x = number)|
|midireader_man.py|ser = serial.Serial('dev/ttyAMA0',31250, timeout=1)| change serial name to COMx (x = number)|


## Find Serial Port
Linux
``` 
ls dev/tty*
```

Windows
``` 

```

## Limitation (Potential Further Development)

- Lack of error handling management
- It will continue to play when the pause button is pressed (if the microcontroller is still in the ON state before pausing)
- Needs a major refactoring