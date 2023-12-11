# Digital Audio Processing Functions for RuHuman (daps.py)
# Author: Timothy Do

import os
import shutil

# Converts input audio file (.wav,.mp3,etc. into a flac for ASVSpoof)
def inputToFlac(inputPath):
	if(shutil.which('ffmpeg') is not None):
		os.system(f"ffmpeg -y -i {inputPath} -sample_fmt s16 -acodec flac -ac 1 -ar 16000 {os.path.splitext(inputPath)[0]}.flac")
	else:
		print('ffmpeg is not installed. Please install it.')
		return False
	return True

def sendToDetector(flacPath,detector):
	pass
	
if __name__ == '__main__':
	inputToFlac('./static/JR.wav')