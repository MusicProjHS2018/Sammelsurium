from __future__ import print_function
import midi

pattern = midi.read_midifile("/home/xhta/Music/MIDI/MAPS_MUS-mond_1_SptkBGAm.mid")

mf = open("/home/xhta/Music/MIDI/mond_MIDI.txt", "w")
print (pattern, file = mf)
