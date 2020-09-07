#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
#from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

import os

# before start:
# - start multimidicast [&]
# - ensure midipipe exists - mkfifo midipipe
# - start amidicat - ./amidicat --port 128:0 --hex < ./midipipe

import midi_notes

# needed for the laser harp - minimal ambient reading that is considered to be an "untouched chord"
# will try to add a motor to allow "on stage" adjustments
AMBIENT_THRESHOLD = 11

# check if multimidicast is running and start it if not
if os.popen('pgrep multimidicast').read().strip() == '':
    os.system('./multimidicast &')
    print('multimidicast started')
else:
    print('multidicast was running')

wait(500)

# check if midipipe was created
if os.popen('ls midipipe').read().strip() == 'midipipe':
    print('midipipe exists')
else:
    os.system('mkfifo midipipe')
    print('midipipe created')

# check if amidicat is running and start it if not
print(os.popen('pgrep amidicat').read().strip())

if os.popen('pgrep amidicat').read().strip() == '':
    os.system('./amidicat --port 128:0 --hex < ./midipipe &')
    print('amidicat started')
else:
    print('amidicat was running')

print(os.popen('pgrep amidicat').read().strip())

ev3 = EV3Brick()
ts1 = ColorSensor(Port.S1)    # lazy copy... need to change the names
ts2 = ColorSensor(Port.S2)
ts3 = ColorSensor(Port.S3)
ts4 = ColorSensor(Port.S4)

# notes associated to each sensor
my_notes = [midi_notes.C4, midi_notes.D4, midi_notes.E4, midi_notes.F4]
#my_notes = [midi_notes.G4, midi_notes.A4, midi_notes.B4, midi_notes.C5]

ALL_NOTES_OFF = "B0 7B 00"

def send_note_on(note):
    if note in my_notes:
        pipe.write("90 " + note + " 7F")
    else:
        # mistake ?
        pipe.write(ALL_NOTES_OFF)

def send_note_off(note):
    if note in my_notes:
        pipe.write("80 " + note + " 00")
    else:
        # mistake ?
        pipe.write(ALL_NOTES_OFF)

key_1_on = False
key_2_on = False
key_3_on = False
key_4_on = False

pipe = open("./midipipe", "w")
send_note_off('ALL')
while True :
    if ts1.ambient() < AMBIENT_THRESHOLD :
        if key_1_on == False :
            send_note_on(my_notes[0])
            key_1_on = True
    else:
        if key_1_on == True :
            send_note_off(my_notes[0])
            key_1_on = False

    if ts2.ambient() < AMBIENT_THRESHOLD :
        if key_2_on == False :
            send_note_on(my_notes[1])
            key_2_on = True
    else:
        if  key_2_on == True :
            send_note_off(my_notes[1])
            key_2_on = False

    if ts3.ambient() < AMBIENT_THRESHOLD :
        if key_3_on == False :
            send_note_on(my_notes[2])
            key_3_on = True
    else:
        if key_3_on == True :
            send_note_off(my_notes[2])
            key_3_on = False

    if ts4.ambient() < AMBIENT_THRESHOLD :
        if key_4_on == False :
            send_note_on(my_notes[3])
            key_4_on = True
    else:
        if key_4_on == True :
            send_note_off(my_notes[3])
            key_4_on = False

#it never gets here but it is important to do this on exit
send_note_off('ALL')
pipe.close()
