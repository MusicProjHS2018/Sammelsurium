# Sammelsurium
Code Fragmente 

start readMIDI.py 
like 
python2.7 readMIDI.py moonlightsonata.mid
will create a textfile moonlightsonata_MIDI.txt 
does not support python3. needs package Py-midi (https://github.com/vishnubob/python-midi.git)



start readwave.py
like
python readwav.py moonlightsonata.wav
will create a textfile moonlightsonata_WAV.txt containing the first 100000 samples


added downsampling.py on 23 Dec 2018
need pysound package
tested on mond bach 846 and chopin p7: downsampling from 44.1 kH to 16 kHz, file size becomes 0.3628 of orig size
output file still sounds good 
