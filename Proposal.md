# Project Proposal

## Motivation and Objective
The advent of generative AI is inevitable when generating synthetic data to bypass certain human verification systems. Current liveness detection systems that use biometric sensors (e.g. fingerprint, face, voice sensors) are always vulnerable to being bypassed with spoofing methods like photos, face masks, and voice clones.

The objective of RuHuman is to evaluate/refine existing verification systems that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by some other medium (e.g. recording playback or synthesized with generative AI). Additionally, the project aims to be easily accessible to the general public, being able to be employed on any client wireless device that has a microphone. This makes liveness detection versatile in many environments such as robocalls & virtual interviews.

## State of the Art and Its Limitations
Audio ASVSpoof (Automatic Speaker Verification and Spoofing Countermeasure Challenge) is a dedicated challenge that gathers researchers from around the world to developing audio spoofing pipelines. The two problems explored in this challenge are Logical Access (LA) attacks (Speech Synthesis/Voice Conversions) and Physical Attacks (PA) (Replay through Speaker). Researchers have presented audio encoding schemes such as MFCC (Mel-frequency cepstral coefficients) & Spectrogram graphs to augment training their classifiers for detection. The limits of the practice is that some datasets used for training in the competition were in a controlled environment, which limits the effect of alternative additive sources in real-world applications (e.g. noise, multi-speakers, nature).

## Novelty & Rationale
The approach of RuHuman is to first evaluate the performance of existing submissions of the ASVSpoof competitions with a custom dataset with audio samples that have alternative additive sound sources along with the speaker source. Additionally, the custom dataset will have their audio samples from real speakers and synthesized with some of the most popular voice cloning software (e.g. Apple Personal Voice, TortoiseTTS, RVC).  Afterwards, optimization of training the baseline LA/PA classifier models (based on MFCC) will be based on augmenting the training data with additive sound sources to increase robustness of environments for detection accuracy. This should make the ASVspoof models more adaptable in versatile environments.

## Potential Impact
If this project yields success, the approach should indicate to researchers in the ASVspoof competition that the technical factors of additive sound sources is imperative for implementing their submissions in real-world environments. On a more broader sense, the user interface that will be implemented should make it easy for the general public to assess if their audio files were uttered by a real human. They should be able to access audio liveness detection from a large range of computing: from a smartphone to an audio workstation.

## Challenges
Potential challenges when evaluating these audio liveness detection systems come from advanced spoof attacks such as multi-speakers. For instance, a real human can utter a words for the first few seconds in the sample, and then generative AI can synthesize the rest of the audio, leading to the system potentially classifying the sample only based on the initial audio samples. Another way for a potential spoof is if a human and  generative AI spoke concurrently, it can produce a hidden set, potentially leading to a false positive classification. 

## Requirements for Success
In the development of this project, a strong command of Digital Speech Processing is required when working with analysis of audio files. Specifically, knowledge of STFT (short-time Fourier Transform) and other frequency based audio encodings will be applied in many of these implementations. Knowledge of neural network architectures are useful for training the detector to infer on real-world audio samples.

Hardware resources to development RuHuman are NVIDIA GPU(s) with high VRAM (e.g. NVIDIA RTX 3090) for their acceleration improvements performing convolution. Software resources for RuHuman include Pytorch which is the code baseline for many of the deepfake voice detectors/synthesizers. The program dependencies of this project are the various deepfake voice cloning programs (e.g. Apple Personal Voice, TortoiseTTS, RVC) and voice detectors submitted to ASVSpoof.

## Metrics of Success
The success for evaluating each of the submissions of ASVSpoof is to evaluate them against the tandem detection cost function (t-DCF) formulated by the authors of ASVSpoof. Secondary metrics to evaluate success with be the equal error rate (EER) and computation time of each submission. These metrics will be computed with respect to the custom dataset mentioned in the previous sections of this proposal.

## Execution Plan
For developing the framework of this project, the key tasks are divided up in the following sequential list:

1. Experiment with deepfake voice cloners and be able to generate a voice model that can plausibly synthesize a real sounding voice model.
2. Experiment with various ASVSpoof submissions with the ASVSpoof dataset.
3. Preparing the Custom Dataset with a variety of deepfake voice cloners and augmenting the dataset with addivite sound souces (e.g. noise, background, etc.)
4. Evaluate various ASVSpoof submissions with custom generated dataset. 
5. Develop a user interface where a device upload audios to determine liveness detection.
6. Fine-tune ASVSpoof detection models for more advanced spoofing attacks.

## Related Work

### 9.a. Papers
[1] Most recent outline of ASVspoof: Automatic Speaker Verification and Spoofing Countermeasures Challenge <br>

[2] This paper uses MFCC Spectrogram/Frequency Domain Analysis to provide different audio encodings to detect Deepfake Audio <br>


[3] This paper uses prior speaker Samples to verify the speaker <br>

[4] This paper exploits the multi-modalities of Audio with Video Multimodal Learning for better liveness detection. 

[5] This paper changes verification pipeline by creating random challenges for a human user to do but the AI can't do: D-CAPTCHA. <br>

[6] Realtime Audio Deepfake Detection, helpful in understanding how liveness can be detected in realtime. <br>

### 9.b. Datasets
[7] The project will maninly use the main ASVSpoof Dataset from 2019 for the Logical Access (LA) challenge. <br>

### 9.c. Software
[8] Paper for the Pytorch Framework <br>

[9] Paper for Tortoise-TTS  <br>

[10] Paper for Retrieval-based-Voice-Conversion (RVC) <br>

## References
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