# Digital Audio Processing Functions for RuHuman (daps.py)
# Author: Timothy Do

import os
import shutil
import sys
import torch
import torch.nn.functional as F
import torchaudio

import librosa
import numpy as np
import matplotlib.pyplot as plt


# Add Detector Pipelines 
sys.path.append('../Detectors/Tortoise/')
import classify


# Converts input audio file (.wav,.mp3,etc. into a flac for ASVSpoof Submissions).
def inputToFlac(inputPath):
	flacPath = f'{os.path.splitext(inputPath)[0]}.flac'
	if(shutil.which('ffmpeg') is not None):
		os.system(f"ffmpeg -y -i {inputPath} -sample_fmt s16 -acodec flac -ac 1 -ar 16000 {flacPath}")
	else:
		print('ffmpeg is not installed. Please install it.')
	return flacPath

# Converts input audio file from interent into a .wav for streamlined detection
def inputToWav(inputPath):
	wavPath = f'{os.path.splitext(inputPath)[0]}.wav'
	if(shutil.which('ffmpeg') is not None):
		os.system(f"ffmpeg -y -i {inputPath} {wavPath}")
	else:
		print('ffmpeg is not installed. Please install it.')
	return wavPath


# Plots the Mel-Spectrogram of the Input
def plotMelSpectrogram(inputPath):
	plotPath = f'{os.path.splitext(inputPath)[0]}_mel.jpg'
	audio, fs = librosa.load(inputPath)
	melSpectrogram = librosa.power_to_db(librosa.feature.melspectrogram(y=audio,sr=fs),ref=1.0) # Retrieve the Mel-Features in dB
	plt.figure(figsize=(10,4)) 
	librosa.display.specshow(melSpectrogram,x_axis='time',y_axis='mel',sr=fs,cmap='coolwarm')
	plt.colorbar(format='%+2.0f dB')
	plt.title(f'Mel Spectrogram of {os.path.basename(inputPath)}')
	plt.savefig(plotPath)
	return plotPath

# Sends the Audio Path to the Detector to Compute Scores
def sendToDetector(path,detector='Tortoise',convertToFlac=False):
	if(convertToFlac):
		path = inputToFlac(path)
	loadings = {
		'Tortoise': classify.load_tortoise
	}
	detects = {
		'Tortoise': classify.classify_audio_clip
	}
	audio = loadings[detector](path)
	return detects[detector](audio) # Returns a Probablity of Being AI
	
if __name__ == '__main__':
	plotMelSpectrogram('./results/JR.wav')
	#print(sendToDetector('./results/JR.wav'))