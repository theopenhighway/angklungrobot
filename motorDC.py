import time
import board
import pwmio
import analogio
import touchio
import neopixel
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
from adafruit_motor import motor

import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange


