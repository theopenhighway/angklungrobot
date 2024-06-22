# Angklung Robot

## Overview

This is a repository is based on my undergraduate thesis, titled "Perancangan Sistem Otomatisasi Alat Musik Angklung dengan Input Berformat MIDI" (translation: bsbsbbsbbs). It is a system that allows an angklung (Indonesian traditional musical instrument) to operate automatically based on MIDI events.

There are two modes available on this system:

- Read and parse MIDI file
- Sending MIDI events via MIDI controller

## Requirements

- Python 3.9.2 or higher
- Raspbian OS


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
pip install python-rtmidi 
```

pyQt5 version 5.15.9
``` 
pip install python-rtmidi 
```

## Repository Organization



## Limitation (Potential Further Development)

- Lack of error handling management
- 