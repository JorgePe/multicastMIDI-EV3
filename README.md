# multicastMIDI-EV3
Using LEGO MINDSTORMS EV3 as a wireless MIDi instrument (multicast MIDI)

My goal is being able to use LEGO MINDSTOMS EV3 as a MIDI instrument that can play along with other MIDI components.
Music is sent in MIDI format directly, through the network, as multimicast MIDI (i.e. ipMIDI).

I only have two MIDI keyboards that my wife uses from time to time. I have no music background so the best I can do with MIDI is preparing a linux laptop with a soft MIDI synth and Rosegarden and watch my wife play some notes and create a music score with it. But a few years ago I made a Laser Harp with LEGO MINDSTORMS EV3 and used MQTT to send commands through Wi-Fi to my laptop where a pyhton script converted those commands to MIDI commands... the wife enjoyed it so much she keeps asking me to rebuild it.

Now I am sending MIDI commands directly from the EV3 to the soft synth, with multicast MIDI.

Multicast MIDI is not a MIDI standard but there are several applications that make use of it, like TouchDAW. TouchDAW also understands RTP-MIDI so if I ever understand how to send RTP-MIDI messages from ev3dev will try changing this program.

If you are using a computer as a synth (or as a gateway to a real synth) you need to run multimidcast or qmidinet or any other application that can work as multicast MIDI router.

For the moment, I'm using 'pybricks-micropython' included with ev3dev (I'm using stretch snapshot released in 2020-04-10). Unlike full python3 bindings, micropython loads very fast but I didn't figure how to detect when execution ends so I cannot send 'all notes off' to ensure no note gets stuck on the synth side. 

I include these two programs that were built for EV3 from their source code:

- Dirk Jagdmann's multimidicast (https://llg.cubic.org/tools/multimidicast/)
- Josh Lehan's aMIDIcat (http://krellan.com/amidicat/)

You can use more than one EV3 to extend your note range. I'm using it with 2 EV3 each one with 4 touch sensors (a one octave keyboard) and also with
touch colors instead (a one octave light or laser harp).
The setup is the same on each EV3, you just need to change the notes assigned to each touch sensor. I didn't try more EV3 but it should work (except, maybe, for wi-fi limitations to multicast).

I get some notes 'stucked' on the synth size. Not sure if it is my laptop fault or my wireless router fault, usually I just press Rosegarden 'panic' button to clear it. When I was recording my sons playing with it, I noticed that it hapened much more frequently... somehow my smartphone was causing  it.

So I've been reading TouchDAW's FAQ and other posts on the net regarding midicast problems... if you have problems try to disable bluetooth on everything, also keeping the number of Wi-Fi clients as low as possible or even using a dedicated AP just for your MIDI network. Or get and old USB-to-Ethernet adapter and discard Wi-Fi, connect your EV3 to your laptop through a RJ-45 ethernet cable. I considered all these options but after started using a Raspberry Pi with Yoshimi as a softsynth never had problems again. Also trying Zynthian, midicast works fine (got a few Xruns but think it's my USB soundcard's fault).

Details: https://ofalcao.pt/blog/series/lego-ipmidi
