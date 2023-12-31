# Prerequisites 
## Hardware
1. NVIDIA GPU (e.g. NVIDIA RTX 3080) 

## Software
1. Windows 10/11 Operating System
2. [Python Version 3.11](https://www.python.org/downloads/release/python-3110/) (other versions untested)
3. [MATLAB R2023b](https://www.mathworks.com/?s_tid=gn_logo) (other versions untested)
4. [Matlab Engine for Python](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
5. [unzip](https://gnuwin32.sourceforge.net/packages/unzip.htm) 
6. [ffmpeg](https://www.ffmpeg.org/download.html#build-windows)
7. [Git for Windows](https://gitforwindows.org/)

# Installation Instructions

1. First Install the Dependencies by running <code>pip install -r requirements.txt</code>
2. Go to the Cloners folder and run <code>getVoiceCloners.py</code> which downloads the voice cloners and install their dependencies.
3. Go to the Detectors folder and run <code>getVoiceDetectors.py</code> which downloads the voice detectors and install their dependencies.
4. Go to the Samples folder and run <code>getSamples.py</code> which downloads the ASVspoof datasets (may take a long time). If this script doesn't work, you may download & unzip them manually by referring to direct links ([ASVSpoof2019](https://www.asvspoof.org/database) and [ASVSpoof2021](https://zenodo.org/record/4837263)). Once downloaded rename the datasets to <code>ASVSpoof2019LA</code> and <code>ASVSpoof2021LA</code> respectively.
5. Download all keys and metadata for [ASVSpoof2021](https://www.asvspoof.org/index2021.html) under 'Evaluation Keys and MetaData'. Compiled them all under a folder called 'keys' and store them in <code>./Detectors/2021Baseline/eval-package/keys</code>.
6. Move all Refactored files to make the callable functions to the user interface by running <code>refactor.py</code> in the Detector folder.
7. You should be all set to use the user interface! To run the app, go to the UI folder and run <code>RuHumanFlaskAudio.py</code>. The client should be able to access the interface from [http://localhost:8080](http://localhost:8080).
8. Optionally, you can run the app as an https app. To do this, generate certificates by opening Git for Windows, change working directory to the UI folder, then run <code>openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365</code> to generate local https self-signed certificates.
