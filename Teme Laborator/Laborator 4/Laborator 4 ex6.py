import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# sample_rate, audio_signal = wavfile.read('sample.wav')

N = 10000
audio_signal = np.random.randn(N)