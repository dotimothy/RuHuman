echo 2021 Baseline LA CQCC-GMM ASV and EER Results
python main.py --cm-score-file cm_scores/LA_CQCC-GMM_cm_scores.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-CQCC-GMM.npy
echo 2021 Baseline LA LFCC-GMM ASV and EER Results
python main.py --cm-score-file cm_scores/LA_LFCC-GMM_cm_scores.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-LFCC-GMM.npy
echo 2021 Baseline LA RawNet2 ASV and EER Results
python main.py --cm-score-file cm_scores/LA_RawNet2_cm_scores.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-RawNet2.npy
echo 2021 Baseline LA CQCC-GMM ASV and EER Results (with AWGN SNR of 50)
python main.py --cm-score-file cm_scores/LA_CQCC-GMM_cm_scores_awgn_50.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-CQCC-GMM_awgn_50.npy
echo 2021 Baseline LA LFCC-GMM ASV and EER Results (with AWGN SNR of 50)
python main.py --cm-score-file cm_scores/LA_LFCC-GMM_cm_scores_awgn_50.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-LFCC-GMM_awgn_50.npy
echo 2021 Baseline LA RawNet2 ASV and EER Results (with AWGN SNR of 50)
python main.py --cm-score-file cm_scores/LA_RawNet2_cm_scores_awgn_50.txt --track LA --subset eval --recompute-c012 --c012-path cm_scores/LA-RawNet2_awgn_50.npy

