function scores_cm = cqccgmm(filePath)

    addpath(genpath('CQCC'));
    addpath(genpath('GMM'));
    
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
    
    [x,fs] = audioread(filePath);
    
    % featrue extraction
    x_fea = cqcc(x, fs, B, fmax, fmin, d, cf, 'ZsdD');
    
    % score computation
    llk_genuine = mean(compute_llk(x_fea,genuineGMM.m,genuineGMM.s,genuineGMM.w));
    llk_spoof = mean(compute_llk(x_fea,spoofGMM.m,spoofGMM.s,spoofGMM.w));
    
    % compute log-likelihood ratio
    scores_cm = llk_genuine - llk_spoof;
end