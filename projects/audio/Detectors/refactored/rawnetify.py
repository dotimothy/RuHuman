import os 
import torch
import librosa
from torch import nn
from model import RawNet
import yaml
import numpy as np


# Adopted from ASVSpoof2021 RawNet2
def pad(x, max_len=64600):
    x_len = x.shape[0]
    if x_len >= max_len:
        return x[:max_len]
    # need to pad
    num_repeats = int(max_len / x_len)+1
    padded_x = np.tile(x, (1, num_repeats))[:, :max_len][0]
    return padded_x	

def classify(audioPath):
    modelPath = f'{os.path.dirname(os.path.abspath(__file__))}/pre_trained_DF_RawNet2/pre_trained_DF_RawNet2.pth'
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    dir_yaml = f'{os.path.dirname(os.path.abspath(__file__))}/{os.path.splitext("model_config_RawNet")[0]}.yaml'
    with open(dir_yaml, 'r') as f_yaml:
        parser1 = yaml.load(f_yaml,yaml.Loader)
    model = RawNet(parser1['model'],device)
    model = (model).to(device)
    model.load_state_dict(torch.load(modelPath,map_location=device))
    audio,fs = librosa.load(audioPath)
    #audio = pad(audio)
    audio = torch.Tensor(np.array([audio])).to(device)
    out = model(audio)
    preds = out.data.cpu().numpy().ravel()
    probs = np.exp(preds)
    prob = 1-probs[1]
    return 100*prob

if __name__ == '__main__': 
	print(classify('../../../../Samples/ASVspoof2021LA/ASVspoof2021_LA_eval/flac/LA_E_9332881.flac'))
	print(classify('../../../../Samples/ASVspoof2021LA/ASVspoof2021_LA_eval/flac/LA_E_7302969.flac'))