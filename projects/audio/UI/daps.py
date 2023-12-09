# Digital Audio Processing Functions for RuHuman (daps.py)
# Author: Timothy Do

import os

# Converts input audio file (.wav,.mp3,etc. into a flac for ASVSpoof)
def inputToFlac(inputPath):
	os.system(f"ffmpeg -y -i {inputPath} -sample_fmt s16 -acodec flac -ar 16000 {os.path.splitext(inputPath)[0]}.flac")

def sendToDetector(flacPath,detector):
	pass
	
if __name__ == '__main__':
	inputToFlac('./static/JR.wav')