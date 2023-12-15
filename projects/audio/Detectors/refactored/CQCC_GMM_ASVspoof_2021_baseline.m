%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CQCC-GMM ASVspoof 2021 baseline 
%
% Logical Access (LA) task
%
% http://www.asvspoof.org/
%
% ============================================================================================
% Matlab implementation of spoofing detection baseline system based on:
% front-end:
%   - high-time resolution constant Q cepstral coefficients (CQCCs)
% back-end:
%   - Gaussian Mixture Models (GMMs)
% ============================================================================================
% by Massimiliano Todisco - EURECOM (France) - 2021
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear; close all; clc;

% add required libraries to the path
addpath(genpath('CQCC'));
addpath(genpath('GMM'));

%% TODO: set paths to the audio files, protocols and feature and GMM configuration
% in this code we assume that the data follows the directory structure:
%
% ASVspoof2021_root/
%   |- LA
%      |- ASVspoof2021_LA_eval/
% ASVspoof2019_root/
%   |- LA
% 	   |- ASVspoof2019_LA_cm_protocols/
% 	   |- ASVspoof2019_LA_train/

use_preTrained_models = true; % use pre-trained models

% set here the path and the name of the scoring file
LA_scoring_path = 'LA_cm_scores';
LA_scoring_filename = 'LA_CQCC-GMM_cm_scores_awgn_50.txt';

% set here the path to the databases and protocol files
pathToASVspoof19 = '../../../../../Samples/ASVSpoof2019LA';
pathToASVspoof21 = '../../../../../Samples/ASVSpoof2021LA';

if use_preTrained_models
    
    % feature configuration
    B = 12;             % number of bins per octave
    fmin = 62.50;       % lowest frequency to be analyzed
    fmax = 4000;        % highest frequency to be analyzed
    d = 16;             % number of uniform samples in the first octave
    cf = 19;            % number of cepstral coefficients excluding 0'th coefficient
    
    if ~exist('preTrained','dir')
        mkdir('preTrained');
    end    
    
    if ~exist('preTrained/pre_trained_LA_CQCC-GMM.mat','file')
        url = 'http://www.asvspoof.org/asvspoof2021/pre_trained_LA_CQCC-GMM.zip';
        outfilename = websave('preTrained/pre_trained_LA_CQCC-GMM.zip',url);
        unzip(outfilename,'preTrained');
    end
    
    load preTrained/pre_trained_LA_CQCC-GMM.mat
    
else
    
    % feature configuration
    B = 12;             % number of bins per octave
    fmin = 62.50;       % lowest frequency to be analyzed
    fmax = 4000;        % highest frequency to be analyzed
    d = 16;             % number of uniform samples in the first octave
    cf = 19;            % number of cepstral coefficients excluding 0'th coefficient
    
    % GMM configuration
    no_components = 512;
    max_iterations = 10;
    
    % downsampling training factor
    bonafide_ds_factor = 1; % downsampling factor for bonafide data
    spoof_ds_factor = 10; % downsampling factor for spoof data
    
    % Read train protocol
    pathToDatabase19 = fullfile(pathToASVspoof19, 'LA');
    trainProtocolFile = fullfile(pathToDatabase19, 'ASVspoof2019_LA_cm_protocols', 'ASVspoof2019.LA.cm.train.trn.txt');
    
    % read train protocol
    fileID = fopen(trainProtocolFile);
    protocol = textscan(fileID, '%s%s%s%s%s');
    fclose(fileID);
    
    % get file and label lists
    filelist = protocol{2};
    key = protocol{5};
    
    % get indices of genuine and spoof files
    bonafideIdx = find(strcmp(key,'bonafide'));
    spoofIdx = find(strcmp(key,'spoof'));
    
    % downsampling training data
    bonafideIdx = bonafideIdx(1:bonafide_ds_factor:size(bonafideIdx));
    spoofIdx = spoofIdx(1:spoof_ds_factor:size(spoofIdx));
    
    % Feature extraction for training data
    % extract features for GENUINE training data and store in cell array
    disp('Extracting features for BONA FIDE training data...');
    genuineFeatureCell = cell(size(bonafideIdx));
    parfor i=1:length(bonafideIdx)
        filePath = fullfile(pathToASVspoof19,'LA','ASVspoof2019_LA_train/flac',[filelist{bonafideIdx(i)} '.flac']);
        [x,fs] = audioread(filePath);
        
        % featrue extraction
        genuineFeatureCell{i} = cqcc(x, fs, B, fmax, fmin, d, cf, 'ZsdD');
    end
    disp('Done!');
    
    % extract features for SPOOF training data and store in cell array
    disp('Extracting features for SPOOF training data...');
    spoofFeatureCell = cell(size(spoofIdx));
    parfor i=1:length(spoofIdx)
        filePath = fullfile(pathToASVspoof19,'LA','ASVspoof2019_LA_train/flac_noisy',[filelist{bonafideIdx(i)} '.flac']);
        [x,fs] = audioread(filePath);
        
        % featrue extraction
        spoofFeatureCell{i} = cqcc(x, fs, B, fmax, fmin, d, cf, 'ZsdD');
    end
    disp('Done!');
    
    % GMM training
    % train GMM for BONA FIDE data
    disp('Training GMM for BONA FIDE...');
    [genuineGMM.m, genuineGMM.s, genuineGMM.w] = vl_gmm([genuineFeatureCell{:}], no_components, 'verbose', 'MaxNumIterations',max_iterations);
    disp('Done!');
    
    % train GMM for SPOOF data
    disp('Training GMM for SPOOF...');
    [spoofGMM.m, spoofGMM.s, spoofGMM.w] = vl_gmm([spoofFeatureCell{:}], no_components, 'verbose', 'MaxNumIterations',max_iterations);
    disp('Done!');
end

% Read eval protocol
pathToDatabase21 = fullfile(pathToASVspoof21, '');
evalProtocolFile = fullfile(pathToDatabase21, 'ASVspoof2021_LA_eval', 'ASVspoof2021.LA.cm.eval.trl.txt');
disp(evalProtocolFile);

%% Feature extraction and scoring of eval data

% read evaluation protocol
fileID = fopen(evalProtocolFile);
protocol = textscan(fileID, '%s');
fclose(fileID);

% get file name
filelist = protocol{1};

% process each evaluation trial: feature extraction and scoring
scores_cm = zeros(size(filelist));
disp('Computing scores for eval trials...');
parfor i=1:length(filelist)
    filePath = fullfile(pathToDatabase21,'ASVspoof2021_LA_eval/flac_noisy',[filelist{i} '.flac']);
    [x,fs] = audioread(filePath);
    
    % featrue extraction
    x_fea = cqcc(x, fs, B, fmax, fmin, d, cf, 'ZsdD');
    
    % score computation
    llk_genuine = mean(compute_llk(x_fea,genuineGMM.m,genuineGMM.s,genuineGMM.w));
    llk_spoof = mean(compute_llk(x_fea,spoofGMM.m,spoofGMM.s,spoofGMM.w));
    
    % compute log-likelihood ratio
    scores_cm(i) = llk_genuine - llk_spoof;
end
disp('Done!');

% save scores to disk
disp('Saving the scoring file to disk...');
if ~exist(LA_scoring_path,'dir')
    mkdir(LA_scoring_path);
end
fid = fopen(fullfile(LA_scoring_path,LA_scoring_filename), 'w');
for i=1:length(scores_cm)
    fprintf(fid,'%s %.6f\n',filelist{i},scores_cm(i));
end
fclose(fid);
disp('Done!');
