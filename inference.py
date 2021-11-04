import matplotlib
import matplotlib.pylab as plt

import IPython.display as ipd

import sys
sys.path.append('waveglow/')
import numpy as np
import torch

from hparams import create_hparams
from model import Tacotron2
from layers import TacotronSTFT, STFT
from audio_processing import griffin_lim
from train import load_model
from text import text_to_sequence
from denoiser import Denoiser


def plot_data(data, figsize=(16, 4)):
    fig, axes = plt.subplots(1, len(data), figsize=figsize)
    for i in range(len(data)):
        axes[i].imshow(data[i], aspect='auto', origin='lower',
                       interpolation='none')

hparams = create_hparams()
hparams.sampling_rate = 22050

text = "ba là con cá mập , mẹ là con cá heo , con là con cá kình , ba con cá hung hắng , đốt cháy một ngôi nhà , ăn hết một con bò ."
#print(text)
sequence = np.array(text_to_sequence(text, ['basic_cleaners']))[None, :]
#print(sequence)
#exit()
sequence = torch.autograd.Variable(
    torch.from_numpy(sequence)).long()

checkpoint_path = "/storage/vangt/TTS/tacotron2/output_vi/checkpoint_50000"
model = load_model(hparams)
model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
_ = model.cuda().eval().half()


waveglow_path = 'waveglow_256channels_universal_v5.pt'
waveglow = torch.load(waveglow_path)['model']
waveglow.cuda().eval().half()
for k in waveglow.convinv:
    k.float()
#denoiser = Denoiser(waveglow)

mel_outputs, mel_outputs_postnet, _, alignments = model.inference(sequence)
plot_data((mel_outputs.float().data.cpu().numpy()[0],
           mel_outputs_postnet.float().data.cpu().numpy()[0],
           alignments.float().data.cpu().numpy()[0].T))


with torch.no_grad():
    audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
ipd.Audio(audio[0].data.cpu().numpy(), rate=hparams.sampling_rate)

#audio_denoised = denoiser(audio, strength=0.01)[:, 0]
#ipd.Audio(audio_denoised.cpu().numpy(), rate=hparams.sampling_rate)
ipd.Audio(audio.cpu().numpy(), rate=hparams.sampling_rate)