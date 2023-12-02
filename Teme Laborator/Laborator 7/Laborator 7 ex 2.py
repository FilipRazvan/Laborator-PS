from scipy import fftpack
from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

# imaginea data
X = misc.face(gray=True)

# transf fourier bidimensionala
X_fft = fftpack.fft2(X)

# calc spectrul de amplitudine
spectru_amplitudine = np.abs(X_fft)

# calculam SNR
# Cu cat
pragSNR = 0.01 * spectru_amplitudine.max()

# aplicam un filtru lowpass prin eliminarea componentelor de frecventa mare din poza
X_fft_lowpass = X_fft * (spectru_amplitudine > pragSNR)

# Transf inversa fourier pentru a obtine imaginea comprimata
X_compressed = np.real(fftpack.ifft2(X_fft_lowpass))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(X, cmap=plt.cm.gray)
plt.title('Imaginea originala')

plt.subplot(1, 2, 2)
plt.imshow(X_compressed, cmap=plt.cm.gray)
plt.title('Imaginea comprimata')

plt.show()
