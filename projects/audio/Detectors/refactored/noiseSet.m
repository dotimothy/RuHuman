clc; close all; clear;

snr = 50;
pathToASVspoof21 = '../../../../../Samples/ASVSpoof2021LA/ASVspoof2021_LA_eval/';
flacPath = fullfile(pathToASVspoof21,'flac');
noisyPath = fullfile(pathToASVspoof21,'flac_noisy');
if ~exist(noisyPath,'dir')
    mkdir(noisyPath)
end 
fileList = dir(fullfile(flacPath,'*.flac'));
parfor i = 1:length(fileList)
    filePath = fullfile(flacPath,fileList(i).name);
    noisePath = fullfile(noisyPath,fileList(i).name);
    [x,fs] = audioread(filePath);
    x = awgn(x,snr);
    audiowrite(noisePath,x,fs);
end
