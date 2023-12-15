function scores_cm = lfccgmm(filePath)

    addpath(genpath('LFCC'));
    addpath(genpath('../../Baseline-CQCC-GMM/matlab/GMM'));
    
    % feature configuration
    window_length = 30; % ms
    NFFT = 1024;        % FFT bins
    no_Filter = 70;     % no of filters
    no_coeff = 19;      % no of coefficients including 0'th coefficient
    low_freq = 0;       % lowest frequency to be analyzed
    high_freq = 4000;   % highest frequency to be analyzed
    
    if ~exist('preTrained','dir')
        mkdir('preTrained');
    end    
    
    if ~exist("preTrained/pre_trained_LA_LFCC-GMM.mat","file")
        url = 'http://www.asvspoof.org/asvspoof2021/pre_trained_LA_LFCC-GMM.zip';
        outfilename = websave('preTrained/pre_trained_LA_LFCC-GMM.zip',url);
        unzip(outfilename,'preTrained');
    end
    
    load preTrained/pre_trained_LA_LFCC-GMM.mat
    
    [x,fs] = audioread(filePath);
    
    % featrue extraction
    [stat,delta,double_delta] = lfcc_bp(x,fs,window_length,NFFT,no_Filter,no_coeff,low_freq,high_freq);
    x_fea = [stat delta double_delta]';
    
    % score computation
    llk_genuine = mean(compute_llk(x_fea,genuineGMM.m,genuineGMM.s,genuineGMM.w));
    llk_spoof = mean(compute_llk(x_fea,spoofGMM.m,spoofGMM.s,spoofGMM.w));
    
    % compute log-likelihood ratio
    scores_cm = llk_genuine - llk_spoof;
end