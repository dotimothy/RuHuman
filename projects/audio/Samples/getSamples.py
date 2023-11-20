import os
import shutil

datasets = {
	"ASVSpoof2019LA": {
		"link": "https://datashare.ed.ac.uk/download/DS_10283_3336.zip",
		"gdown": "1UGs1o2mDiBO9_iaN-0FupS8x0Tkb4xmt",
		"name": "2019 LA ASVSpoof",
		"types": ["LA"]
	}
}

# Note: Does take a long time to download each dataset
def getDatasets():
	#Make Sure to Have gdown,curl, & unzip binaries installed
	for dataset in datasets:
		print(f'Getting the {datasets[dataset]["name"]} Dataset...')
		if(not(os.path.exists(f"{dataset}.zip"))):
			if "gdown" in datasets[dataset]:
				os.system(f'gdown {datasets[dataset]["gdown"]} -o ./{dataset}.zip')
			else:
				os.system(f'curl -o ./{dataset}.zip \"{datasets[dataset]["link"]}\"')
		if(not(os.path.exists(dataset))):
			os.system(f"unzip ./{dataset}.zip -d {dataset}")

if __name__ == '__main__':
	getDatasets()