# multicastMIDI-EV3
Using LEGO MINDSTORMS EV3 as a wireless MIDi instrument (multicast MIDI)

My goal is being able to use LEGO MINDSTOMS EV3 as a MIDI instrument that can play along with other MIDI components.
Music is sent in MIDI form directly, through the network, as multimicast MIDI (i.e. ipMIDI).

I only have two MIDI keyboards that my wife uses from time to time. I have no music background so the best I can do with MIDI is preparing a linux laptop with a soft MIDI synth and Rosegarden and wath my wife play some notes and create a music score with it. But I made a few years ago a Laser Harp with LEGO MINDSTORMS EV3 and used MQTT to send commands through Wi-Fi to my laptop where a pyhton script converted those commands to MIDI commands.

Now I am trying to send MIDI commands directly from the EV3 to the soft synth, with multicast MIDI.

Multicast MIDI is not a MIDI standard but there are several applications that makes use of it, like TouchDAW. TouchDAW also understands RTP-MIDI and if I ever understand how to send RTP-MIDI messages from ev3dev will try change this program.

If you are using a computer as s synth (or as a gateway to a real synth) you need to run multimidcast or qmidinet or any other application that can work as multicast MIDI router.

For the moment, it uses 'pybricks-micropython' library included with ev3dev (I'm using stretch snapshot released in 2020-04-10). Unlike full python3 bindings, micropython loads very fast but I didn't figure how to detect when execution ends so I cannot send 'all notes off' to ensure no note gets stuck on the synth side. 

I include these two commands that were built for EV3 from their source code:

- Dirk Jagdmann's multimidicast (https://llg.cubic.org/tools/multimidicast/)
- Josh Lehan's aMIDIcat (http://krellan.com/amidicat/)

Details: https://ofalcao.pt/blog/series/lego-ipmidi
