import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
inputfilename= (input("name of song"))
audio, sr = librosa.load('"C:\\Users\\kiran\\Downloads\\astrid.m3u"', sr=44100)
vocals, _ = librosa.effects.hpss(audio)
sf.write(f'Music\\{inputfilename} vocals.wav', vocals, sr)

#python doesnt like single back salshes in paths so use "\\" 
# for example: c:\\users\\blahblah\\music-file 

