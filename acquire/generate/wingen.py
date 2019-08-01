from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

"""
 Generates audio files using SAPI.SpVoice (TTS) by feeding words (per line) in abuses.txt text file
"""

Engine = CreateObject("SAPI.SpVoice")
Stream = CreateObject("SAPI.SpFileStream")
infile = open("abuses.txt", 'r').read()
split = infile.split('\n')
outfile = "{}.wav"

for i in split:
    out = outfile.format(i)
    Stream.Open(out, SpeechLib.SSFMCreateForWrite)
    Engine.AudioOutputStream = Stream
    Engine.speak(i)
    Stream.Close()
    print('Saved {} ...'.format(out))