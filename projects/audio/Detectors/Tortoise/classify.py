import argparse

import torch
import torch.nn.functional as F
from tortoise.utils.audio import load_audio
from tortoise.models.classifier import AudioMiniEncoderWithClassifierHead
import os


def classify_audio_clip(clip):
    
    """
    Returns whether or not Tortoises' classifier thinks the given clip came from Tortoise.
    :param clip: torch tensor containing audio waveform data (get it from load_audio)
    :return: True if the clip was classified as coming from Tortoise and false if it was classified as real.
    """
    modelPath = f'{os.path.dirname(os.path.abspath(__file__))}./classifier.pth'
    classifier = AudioMiniEncoderWithClassifierHead(2, spec_dim=1, embedding_dim=512, depth=5, downsample_factor=4,
                                                    resnet_blocks=2, attn_blocks=4, num_attn_heads=4, base_channels=32,
                                                    dropout=0, kernel_size=5, distribute_zero_label=False)
    classifier.load_state_dict(torch.load(modelPath, map_location=torch.device('cpu')))
    clip = clip.cpu().unsqueeze(0)
    results = F.softmax(classifier(clip), dim=-1)
    return results[0][0]

def load_tortoise(clipPath):
    clip = load_audio(clipPath, 24000)
    clip = clip[:, :220000] if len(clip) > 220000 else clip
    return clip




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--clip', type=str, help='Path to an audio clip to classify.', default="./test.wav")
    args = parser.parse_args()
    clip = load_tortoise(args.clip)
    prob = classify_audio_clip(clip)
    print(f"This classifier thinks there is a {prob*100}% chance that this clip was generated from Tortoise.")