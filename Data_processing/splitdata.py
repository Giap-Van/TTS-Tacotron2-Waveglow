import pandas as pd
import os

data = pd.read_csv('/storage/vangt/TTS/female/metadata.csv', sep='|', header=None)

# Suffle
data = data.sample(frac=1)

train_ratio = 0.8
train_index = int(train_ratio * len(data))

with open('/storage/vangt/TTS/training.txt', 'w') as fd:
    for i, fname in enumerate(data[0][:train_index]):
        PATH = os.path.join(os.getcwd(), 'female/wavs')
        fd.write('{}|{}\n'.format(os.path.join(PATH, fname), data[1][i]))

with open('/storage/vangt/TTS/testing.txt', 'w') as fd:
    for i, fname in enumerate(data[0][train_index:]):
        PATH = os.path.join(os.getcwd(), 'female/wavs')
        fd.write('{}|{}\n'.format(os.path.join(PATH, fname), data[1][i]))
