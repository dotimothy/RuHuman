# Project Proposal

## Motivation and Objective
The advent of generative AI is inevitable when generating synthetic data to bypass certain human verification systems. Current liveness detection systems that use biometric sensors (e.g. fingerprint, face, voice sensors) are always vulnerable to being bypassed with spoofing methods like photos, face masks, and voice clones.

The objective of RuHuman is to evaluate/refine existing verification systems that exploit the multimodalities of audio data in order to establish a strong multi-factored conviction on deciding if the input is being lively uttered by a human or by some other medium (e.g. recording playback or synthesized with generative AI). Additionally, the project aims to be easily accessible to the general public, being able to be employed on any client wireless device that has a microphone. This makes liveness detection versatile in many environments such as robocalls & virtual interviews.

## State of the Art and Its Limitations
Audio ASVSpoof (Automatic Speaker Verification and Spoofing Countermeasure Challenge) is a dedicated challenge that gathers researchers from around the world to developing audio spoofing pipelines. The two problems explored in this challenge are Logical Access (LA) attacks (Speech Synthesis/Voice Conversions) and Physical Attacks (PA) (Replay through Speaker). Researchers have presented audio encoding schemes such as MFCC (Mel-frequency cepstral coefficients) & Spectrogram graphs to augment training their classifiers for detection. The limits of the practice is that some datasets used for training in the competition were in a controlled environment, which limits the effect of alternative additive sources in real-world applications (e.g. noise, multi-speakers, nature).

## Novelty & Rationale
The approach of RuHuman is to first evaluate the performance of existing submissions of the ASVSpoof competitions with a custom dataset with audio samples that have alternative additive sound sources along with the speaker source. Additionally, the custom dataset will have their audio samples from real speakers and synthesized with some of the most popular voice cloning software (e.g. Apple Personal Voice, TortoiseTTS, RVC).  Afterwards, optimization of training the baseline LA/PA classifier models (based on MFCC) will be based on augmenting the training data with addivite sound sources to increase robustness of environments for detection accuracy. This should make the ASVspoof models more adaptable in versatile environments.

## Potential Impact
If this project yields success, the approach should indicate to researchers in the ASVspoof compeitition that the technical factors of additive sound sources is imperative for implementing their submissions in real-world environments. On a more broader sense, the user interface that will be implemented should make it easy for the general public to assess if their audio files were uttered by a real human. They should be able to access audio liveness detection from a large range of computing: from a smartphone to an audio workstation.

## Challenges
Potential challenges when developing audio liveness detection systems come from advanced spoof attacks such as multi-speakerspoofing. For instance, a real human can utter a words for the first few seconds in the sample, and then generative AI can synthesize the rest of the audio,leading to the system potentially classifying the sample only based on the initial audio samples. Another way for a potential spoof is if a human and  generative AI spoke concurrently, it can produce a hidden set, potentially leading to a false positive classification. 

Speaking of false positives, potential risks arise from audio deepfake false classification

## Requirements for Success
What skills and resources are necessary to perform the project?

## Metrics of Success
What are metrics by which you would check for success?

## Execution Plan
Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks.

## Related Work
1. Using MFCC Spectrogram/Frequency Domain Analysis to provide different formats to detect Deepfake Audio <br>
A. Hamza et al., "Deepfake Audio Detection via MFCC Features Using Machine Learning," in IEEE Access, vol. 10, pp. 134018-134028, 2022, doi: 10.1109/ACCESS.2022.3231480.

2. Using Prior Speaker Samples to verify the Speaker <br>
A. Pianese, D. Cozzolino, G. Poggi and L. Verdoliva, "Deepfake audio detection by speaker verification," 2022 IEEE International Workshop on Information Forensics and Security (WIFS), Shanghai, China, 2022, pp. 1-6, doi: 10.1109/WIFS55849.2022.9975428.

3. Creating Random Challenges for a Human User to Do but the AI can't Do: D-CAPTCHA <br>
Lior Yasur, Guy Frankovits, Fred M. Grabovski, and Yisroel Mirsky. 2023. Deepfake CAPTCHA: A Method for Preventing Fake Calls. In ACM ASIA Conference on Computer and Communications Security (ASIA CCS '23), July 10--14, 2023, Melbourne, VIC, Australia. ACM, New York, NY, USA 15 Pages. [https://doi.org/10.1145/3579856.3595801](https://doi.org/10.1145/3579856.3595801)

4. Audio + Video Multimodal Learning for Recognition <br>
Y. Mroueh, E. Marcheret and V. Goel, "Deep multimodal learning for Audio-Visual Speech Recognition," 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), South Brisbane, QLD, Australia, 2015, pp. 2130-2134, doi: 10.1109/ICASSP.2015.7178347.


## References
1. ASVspoof: Automatic Speaker Verification and Spoofing Countermeasures Challenge:
X. Liu et al., "ASVspoof 2021: Towards Spoofed and Deepfake Speech Detection in the Wild," in IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 31, pp. 2507-2522, 2023, doi: 10.1109/TASLP.2023.3285283.
