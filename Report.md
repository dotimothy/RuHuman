# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract
The advent of generative AI is inevitable when generating synthetic data to bypass certain human verification systems. The objective of RuHuman is to evaluate/refine existing verification systems presented in ASVSpoof that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by an audio deepfake. The plan is generate samples with top of the line software in voice cloning (e.g. TortoiseTTS), then evaluate the standard CM/ASV metrics among different pretrained detector architectures with the ASVSpoof2021 evaluation set & make a adaptable user interface that allows any wireless device with a microphone employ these systems in versatile environments.


# 1. Introduction

This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

The objective of RuHuman is to evaluate/refine existing verification systems that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by some other medium (e.g. recording playback or synthesized with generative AI). Additionally, the project aims to be easily accessible to the general public, being able to be employed on any client wireless device that has a microphone. This makes liveness detection versatile in many environments such as robocalls & virtual interviews.

Audio ASVSpoof (Automatic Speaker Verification and Spoofing Countermeasure Challenge) is a dedicated challenge that gathers researchers from around the world to developing audio spoofing pipelines. The two problems explored in this challenge are Logical Access (LA) attacks (Speech Synthesis/Voice Conversions) and Physical Attacks (PA) (Replay through Speaker). Researchers have presented audio encoding schemes such as MFCC (Mel-frequency cepstral coefficients) & Spectrogram graphs to augment training their classifiers for detection. The limits of the practice is that some datasets used for training in the competition were in a controlled environment, which limits the effect of alternative additive sources in real-world applications (e.g. noise, multi-speakers, nature).

The approach of RuHuman is to first evaluate the performance of existing submissions of the ASVSpoof competitions with a custom dataset with audio samples that have alternative additive sound sources along with the speaker source. Additionally, the custom dataset will have their audio samples from real speakers and synthesized with some of the most popular voice cloning software (e.g. Apple Personal Voice, TortoiseTTS, RVC).  Afterwards, optimization of training the baseline LA/PA classifier models (based on MFCC) will be based on augmenting the training data with additive sound sources to increase robustness of environments for detection accuracy. This should make the ASVspoof models more adaptable in versatile environments.

If this project yields success, the approach should indicate to researchers in the ASVspoof competition that the technical factors of additive sound sources is imperative for implementing their submissions in real-world environments. On a more broader sense, the user interface that will be implemented should make it easy for the general public to assess if their audio files were uttered by a real human. They should be able to access audio liveness detection from a large range of computing: from a smartphone to an audio workstation.

Potential challenges when evaluating these audio liveness detection systems come from advanced spoof attacks such as multi-speakers. For instance, a real human can utter a words for the first few seconds in the sample, and then generative AI can synthesize the rest of the audio, leading to the system potentially classifying the sample only based on the initial audio samples. Another way for a potential spoof is if a human and  generative AI spoke concurrently, it can produce a hidden set, potentially leading to a false positive classification. 

The success for evaluating each of the submissions of ASVSpoof is to evaluate them against the tandem detection cost function (t-DCF) formulated by the authors of ASVSpoof. Secondary metrics to evaluate success with be the equal error rate (EER) and computation time of each submission. These metrics will be computed with respect to the custom dataset mentioned in the previous sections of this proposal.

# 2. Related Work

Talk about ASVSpoof2021 summary results in the paper.

# 3. Technical Approach

Explain the pipeline very clearly (from converting the audio file in UI, to generating CM scores, and passing that to t-DCF/EER for results)

# 4. Evaluation and Results

Table with following columns: Author-Architecture | Dataset | t-DCF | EER | Computation Time

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
