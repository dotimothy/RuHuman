import os

cloners = {
	"tortoise-tts": {
		"name": "Tortoise TTS",
		"link": "https://github.com/neonbjb/tortoise-tts",
		"repo": "tortoise-tts",
		"batscript": True 
	}
}

def getVoiceCloners():
	for cloner in cloners.keys(): 
		print(f'Getting the {cloners[cloner]["name"]} Cloner...')
		if(cloners[cloner]["batscript"]):
			os.system(f'setup-{cloners[cloner]["repo"]}.bat')
		else:
			if(not(os.path.exists(cloners[cloner]["repo"]))):
				os.system(f'git clone {cloners[cloner]["link"]} {cloners[cloner]["repo"]}')
			os.chdir(f'{cloners[cloner]["repo"]}')	
			if(os.path.exists('requirements.txt')):
				os.system(f'pip install -r requirements.txt')
			if(os.path.exists('setup.py')):
				os.system(f'python setup.py install')
			os.chdir('..')

# Hopefully this only has to be run once.
if __name__ == '__main__':
	getVoiceCloners()