import os

detectors = {
	"ASVSpoofBaseline2021": {
		"name": "Baseline ASVSpoof 2021",
		"link": "https://github.com/asvspoof-challenge/2021",
		"repo": "2021Baseline",
	},
	"NESL2019": {
		"name": "NESL ASVSpoof 2019",
		"link": "https://github.com/nesl/asvspoof2019",
		"repo": "2019NESL"
	}
}

def getDetectors():
	for detector in detectors.keys():
		if(not(os.path.exists(detectors[detector]["repo"]))):
			print(f'Retrieving the {detectors[detector]["name"]} Detector...')
			os.system(f'git clone {detectors[detector]["link"]} {detectors[detector]["repo"]}')
			if(os.path.exists(f'./{detectors[detector]["repo"]}/requirements.txt')):
				os.system(f'pip install -r ./{detectors[detector]["repo"]}/requirements.txt')

if __name__ == "__main__":
	getDetectors()