import shutil
import os
import getVoiceDetectors

if __name__ == "__main__":
	if(not(os.path.exists('./2021Baseline'))):
		getVoiceDetectors.getDetectors()
	shutil.copyfile('./refactored/computeScores.bat','./2021Baseline/eval-package/computeScores.bat')
	shutil.copyfile('./refactored/cqccgmm.m','./2021Baseline/LA/Baseline-CQCC-GMM/cqccgmm.m')
	shutil.copyfile('./refactored/CQCC_GMM_ASVspoof_2021_baseline.m','./2021Baseline/LA/Baseline-CQCC-GMM/CQCC_GMM_ASVspoof_2021_baseline.m')
	shutil.copyfile('./refactored/lfccgmm.m','./2021Baseline/LA/Baseline-LFCC-GMM/lfccgmm.m')
	shutil.copyfile('./refactored/noiseSet.m','./2021Baseline/LA/Baseline-LFCC-GMM/noiseSet.m')
	shutil.copyfile('./refactored/LFCC_GMM_ASVspoof_2021_baseline.m','./2021Baseline/LA/Baseline-LFCC-GMM/LFCC_GMM_ASVspoof_2021_baseline.m')
	shutil.copyfile('./refactored/main.py','./2021Baseline/LA/Baseline-RawNet2/main.py')
	shutil.copyfile('./refactored/rawnetify.py','./2021Baseline/LA/Baseline-RawNet2/rawnetify.py')
	shutil.copyfile('./refactored/testPipe.bat','./2021Baseline/LA/Baseline-RawNet2/testPipe.bat')
