# Table of Contents
* [Abstract](#abstract)
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract
The advent of generative AI is inevitable when generating synthetic data to bypass certain human verification systems. The objective of RuHuman is to evaluate/refine existing verification systems presented in ASVSpoof that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by an audio deepfake. The technical approach is to generate samples with top of the line software in voice cloning (e.g. TortoiseTTS), then evaluate the standard CM/ASV metrics among different pretrained detector architectures with the ASVSpoof2021 evaluation set & make a adaptable user interface that allows any wireless device with a microphone employ these systems in versatile environments.

# 1. Introduction
The advent of generative AI is inevitable when generating synthetic data to bypass certain human verification systems. With advancements in audio deepfakes, human pereption in distinguishing a real human speaker from an audio deepfake is rapidly increasing in complexity. This is unfourtanely seen in the growing number of audio deepfake crimes, including a [recent story](https://www.youtube.com/watch?v=Dfo2MMGZTvU) on the news highlighting a mother almost being scammed out of $15,000 from a deepfake of her daughter being kidnapped. The assistance of an automated AI-powered audio verification that's easily accessible is essential for mitigating more people from falling victim of these schemes.

The objective of RuHuman is to evaluate/refine existing verification systems that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by some other medium (e.g. recording playback or synthesized with generative AI). Additionally, the project aims to be easily accessible to the general public, being able to be employed on any client wireless device that has a microphone. This makes liveness detection versatile in many environments such as robocalls & virtual interviews.

Audio ASVSpoof (Automatic Speaker Verification and Spoofing Countermeasure Challenge) [1] is a dedicated challenge that gathers researchers from around the world to developing audio spoofing pipelines. The two problems explored in this challenge are Logical Access (LA) attacks (Speech Synthesis/Voice Conversions) and Physical Attacks (PA) (Replay through Speaker). Researchers have presented audio encoding schemes such as MFCC (Mel-frequency cepstral coefficients) & Spectrograms to augment training their classifiers for detection. The limits of the practice is that some datasets used for training in the competition were in a controlled environment, which limits the effect of alternative additive sources in real-world applications (e.g. noise, multi-speakers, nature). RuHuman investigates how additive noise sources effect the performance of systems by injecting them with the audio sample before testing. If this project yields success, the approach should indicate to researchers in the ASVspoof competition that the technical factors of additive sound sources is imperative for training their submissions in real-world environments. On a more broader sense, the user interface that will be implemented should make it easy for the general public to assess if their audio files were uttered by a real human. They should be able to access audio liveness detection from a large range of computing: from a smartphone to an audio workstation.

Potential challenges when evaluating these audio liveness detection systems come from advanced spoof attacks such as multi-speakers. For instance, a real human can utter a words for the first few seconds in the sample, and then generative AI can synthesize the rest of the audio, leading to the system potentially classifying the sample only based on the initial audio samples. Another way for a potential spoof is if a human and generative AI spoke concurrently, it can produce a hidden set, potentially leading to a false positive classification. 

In the development of this project, a strong command of Digital Speech Processing is required when working with analysis of audio files. Specifically, knowledge of STFT (short-time Fourier Transform) and other frequency based audio encodings will be applied in many of these implementations. Knowledge of neural network architectures are useful for training the detector to infer on real-world audio samples. Hardware resources to development RuHuman are NVIDIA GPU(s) with high VRAM (e.g. NVIDIA RTX 3090) for their acceleration improvements performing convolution. Software resources for RuHuman include Pytorch which is the code baseline for many of the deepfake voice detectors/synthesizers. The program dependencies of this project are the various deepfake voice cloning programs (e.g. TortoiseTTS) and voice detectors submitted to ASVSpoof.

The success for evaluating each of the submissions of ASVSpoof is to evaluate them against the tandem detection cost function (t-DCF) formulated by the authors of ASVSpoof. Secondary metrics to evaluate success with be the equal error rate (EER) and computation time of each submission. The objective is to minimize these metrics for efficiency and accuracy. These metrics will be computed with respect to the augmented dataset mentioned previously.

# 2. Related Work

There have been work in ASVSpoof submissions that fuse multiple audio encoding models together in order to further minimize t-DCF and EER metrics. Specifically, an ASVSpoof2019 submission from UCLA NESL (Network and Embedded Systems Laboratory) implemented residual neural networks using ResNet blocks, with the input features being embedded from either log-STFT,  MFCC, or CQCC transforms. 

# 3. Technical Approach

(High-Level Overview of Two Phases). The cloud computer that hosts the Python Flask Server with Classification Backends is equipped with an NVIDIA RTX 3080 GPU.

Overview of Cloners

Overview of Detectors

Overview of User Interface



# 4. Evaluation and Results

## Phase 1: Evaluation of Metrics:
### Accuracy: t-DCF & EER
Tabulated Below are Pooled t-DCF and EERs for the 2021 ASVSpoof Evaluation Set for it's Baseline Models with & without Additive Noise Sources:

| Detector Architecture (Normal)  | Pooled t-DCF | Pooled EER (%)
| ------------- | ------------- | ------------- |
| Baseline LFCC-GMM (MATLAB)  | 0.5758  | 19.30  |
| Baseline CQCC-GMM (MATLAB)  | 0.4964  | 15.62  |
| Baseline RawNet2 (MATLAB)  | 0.4964  | 15.62  |

| Detector Architecture (AWGN)  | Pooled t-DCF | Pooled EER (%)
| ------------- | ------------- | ------------- |
| Baseline LFCC-GMM (MATLAB)  | 0.8527  | 41.33  |
| Baseline CQCC-GMM (MATLAB)  | 0.7609  | 31.99  |
| Baseline RawNet2 (MATLAB)  | 0.3317  | 7.23  |

The full raw CM Scores that generated the above metrics using <code>eval-package</code> can be found in the [results](https://github.com/dotimothy/RuHuman/tree/main/docs/results) folder of this repository.

### Effciency: Computation Time
Tabulated Below are Average Computation Times for verifying a sample from the ASVSpoof2021 dataset. For context, each audio sample is approximately 3-5 seconds in length.

| Detector Architecture  | Average Computation Time (s) |
| ------------- | ------------- 
| Tortoise Audio Mini Encoder (Python)  | 0.22  |
| Baseline LFCC-GMM (MATLAB)  | 0.18  | 
| Baseline CQCC-GMM (MATLAB)  | 0.27  | 
| Baseline RawNet2 (Python)  | 0.30  | 

## Phase 2: Implementation of User Interface
The user interface has been completed and is showcased in the following YouTube video: 
[https://youtu.be/KU3gJ5L9Puw](https://youtu.be/KU3gJ5L9Puw) 
<p align="center">
  <a target="_blank" href="https://youtu.be/KU3gJ5L9Puw"><img src='./docs/media/progress/UI_2.png' width='75%'></a>
</p>

# 5. Discussion and Conclusions

Summarize table, talk about ASVSpoof5 and how we can work on that dataset to improve the models.

# 6. References

[1] X. Liu et al., "ASVspoof 2021: Towards Spoofed and Deepfake Speech Detection in the Wild," in IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 31, pp. 2507-2522, 2023, doi: 10.1109/TASLP.2023.3285283.

[2] A. Hamza et al., "Deepfake Audio Detection via MFCC Features Using Machine Learning," in IEEE Access, vol. 10, pp. 134018-134028, 2022, doi: 10.1109/ACCESS.2022.3231480.

[3] A. Pianese, D. Cozzolino, G. Poggi and L. Verdoliva, "Deepfake audio detection by speaker verification," 2022 IEEE International Workshop on Information Forensics and Security (WIFS), Shanghai, China, 2022, pp. 1-6, doi: 10.1109/WIFS55849.2022.9975428.

[4] Y. Mroueh, E. Marcheret and V. Goel, "Deep multimodal learning for Audio-Visual Speech Recognition," 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), South Brisbane, QLD, Australia, 2015, pp. 2130-2134, doi: 10.1109/ICASSP.2015.7178347.

[5] Lior Yasur, Guy Frankovits, Fred M. Grabovski, and Yisroel Mirsky. 2023. Deepfake CAPTCHA: A Method for Preventing Fake Calls. In ACM ASIA Conference on Computer and Communications Security (ASIA CCS '23), July 10--14, 2023, Melbourne, VIC, Australia. ACM, New York, NY, USA 15 Pages. [https://doi.org/10.1145/3579856.3595801](https://doi.org/10.1145/3579856.3595801)

[6] J. J. Bird and A. Lotfi, Real-time Detection of AI-Generated Speech for DeepFake Voice Conversion. 2023.

[7] Yamagishi, Junichi; Todisco, Massimiliano; Sahidullah, Md; Delgado, Héctor; Wang, Xin; Evans, Nicolas; Kinnunen, Tomi; Lee, Kong Aik; Vestman, Ville; Nautsch, Andreas. (2019). ASVspoof 2019: The 3rd Automatic Speaker Verification Spoofing and Countermeasures Challenge database, [sound]. University of Edinburgh. The Centre for Speech Technology Research (CSTR). https://doi.org/10.7488/ds/2555.

[8] A. Paszke et al., ‘PyTorch: An Imperative Style, High-Performance Deep Learning Library’, in Proceedings of the 33rd International Conference on Neural Information Processing Systems, Red Hook, NY, USA: Curran Associates Inc., 2019.

[9] J. Betker, ‘Better speech synthesis through scaling’, arXiv [cs.SD]. 2023.

[10] RVC-Boss et al., RVC-Project/Retrieval-based-Voice-Conversion-WebUI. 2023. [Online]. Available: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
