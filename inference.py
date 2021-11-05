import matplotlib
matplotlib.use('Agg')

import matplotlib.pylab as plt

import IPython.display as ipd
from IPython.display import Audio

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

from scipy.io.wavfile import write

def plot_data(data, figsize=(16, 4)):
    fig, axes = plt.subplots(1, len(data), figsize=figsize)
    for i in range(len(data)):
        axes[i].imshow(data[i], aspect='auto', origin='lower',
                       interpolation='none')


text = "ba là con cá mập , mẹ là con cá heo , con là con cá kình , ba con cá hung hắng , đốt cháy một ngôi nhà , ăn hết một con bò ."

sequence = np.array(text_to_sequence(text, ['basic_cleaners']))[None, :]

sequence = torch.autograd.Variable(
    torch.from_numpy(sequence)).cuda().long()

def tacotron2_load(path):
    h = create_hparams()
    m = Tacotron2(h)
    m.load_state_dict(torch.load(path)['state_dict'])
    m.to('cuda').eval()

    return m

def waveglow_load(path):
    m = torch.load(path)['model']
    m = m.remove_weightnorm(m)
    m.to('cuda').eval()

    return m


hparams = create_hparams()
hparams.sampling_rate = 22050

checkpoint_path = "/storage/vangt/TTS/tacotron2/output_vi/checkpoint_18000"
tacotron2 = tacotron2_load(checkpoint_path)

waveglow_path = 'waveglow_256channels_universal_v5.pt'
waveglow = waveglow_load(waveglow_path)

with torch.no_grad():
    mel_outputs, mel_outputs_postnet, _, alignments = tacotron2.inference(sequence)
    audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
audio_numpy = audio[0].data.cpu().numpy()


from pydub import AudioSegment
rate = 22050
audio = AudioSegment(audio_numpy.tobytes(), frame_rate=rate, sample_width=audio_numpy.dtype.itemsize, channels=1)
path_audio = '/storage/vangt/TTS/tacotron2/demo_phoneme.wav'
audio.export(path_audio, format='wav')

#audio_numpy = audio[0].data.cpu().numpy()
#audio_numpy = (audio_numpy*32768.0).astype(int)
