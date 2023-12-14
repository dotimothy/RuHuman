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
import csv
import time


# Add Detector Pipelines 
sys.path.append('../Detectors/Tortoise/')
import tortify
import matlab.engine
eng = matlab.engine.start_matlab()


# Converts input audio file (.wav,.mp3,etc. into a flac for ASVSpoof Submissions).
def inputToFlac(inputPath):
	flacPath = f'{os.path.splitext(inputPath)[0]}.flac'
	if(shutil.which('ffmpeg') is not None):
		if(not(os.path.exists(flacPath))):
			os.system(f"ffmpeg -y -i {inputPath} -sample_fmt s16 -acodec flac -ac 1 -ar 16000 {flacPath}")
	else:
		print('ffmpeg is not installed. Please install it.')
	return flacPath

# Converts input audio file from interent into a .wav for streamlined detection
def inputToWav(inputPath):
	wavPath = f'{os.path.splitext(inputPath)[0]}.wav'
	if(shutil.which('ffmpeg') is not None):
		if(not(os.path.exists(wavPath))):
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

def returnPath(path):
	return path

def lfccGMMClassify(path):
	eng.cd('../Detectors/2021Baseline/LA/Baseline-LFCC-GMM/matlab/')
	cm = eng.lfccgmm(f"../../../../../UI/{path}")
	eng.cd('../../../../../UI/')
	return 100/(1+np.exp(-cm)) # Formulation to Convert LLR into a Probablity

def cqccGMMClassify(path):
	eng.cd('../Detectors/2021Baseline/LA/Baseline-CQCC-GMM/matlab/')
	cm = eng.cqccgmm(f"../../../../../UI/{path}")
	eng.cd('../../../../../UI/')
	return 100/(1+np.exp(-cm))  # Formulation to Convert LLR into a Probablity


# Sends the Audio Path to the Detector to Compute Scores
def sendToDetector(path,detector='Tortoise'):
	if(detector != 'Tortoise'):
		path = inputToFlac(path)
	loadings = {
		'Tortoise': tortify.load_tortoise,
		'LFCC-GMM': returnPath,
		'CQCC-GMM': returnPath
	}
	detects = {
		'Tortoise':	tortify.classify_audio_clip,
		'LFCC-GMM': lfccGMMClassify,
		'CQCC-GMM': cqccGMMClassify
	}
	audio = loadings[detector](path)
	return detects[detector](audio) # Returns a Probablity of Being AI

# Computes Probablitly Metric (e.g. CM/EER/t-DCF) and How Long it Takes and Store into a CSV
def computeDetectorMetric(setPath,detector='Tortoise',modelFormat='wav'):
	flacPath = f'{setPath}/flac/'
	wavPath = f'{setPath}/wav/'
	resultCSV = open(f'{setPath}/{os.path.basename(setPath)}_{detector}.csv','w',newline='')
	writer = csv.writer(resultCSV)
	headers = ['Name','CM','Computation Time']
	writer.writerow(headers)
	flacList = [flac for flac in os.listdir(flacPath) if flac.endswith('.flac')]
	if(not(os.path.exists(wavPath))):
		os.mkdir(wavPath)
	for flac in flacList:
		wav = f"{os.path.splitext(flac)[0]}.wav"
		if(not(os.path.exists(f'{wavPath}/{wav}'))) :
			os.system(f'ffmpeg -i {flacPath}/{flac} {wavPath}/{wav}')
	wavList = [wav for wav in os.listdir(wavPath) if wav.endswith('.wav')]
	for wav in wavList: 
		flac = f"{os.path.splitext(wav)[0]}.flac"
		start = time.time()
		cm = sendToDetector(f'{wavPath}/{wav}',detector,detector!='Tortoise')
		duration = time.time() - start
		print(f'{flac} has {cm*100}% of being spoofed by AI ({duration} s)')
		writer.writerow([flac,float(cm),duration])
	resultCSV.close()

if __name__ == '__main__':
	print(float(sendToDetector('./static/LA_E_1000048.wav','CQCC-GMM')))
	#plotMelSpectrogram('./static/Tortoise.mp3')
	#computeDetectorMetric('../Samples/ASVspoof2021LA/ASVspoof2021_LA_eval')