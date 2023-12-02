import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

# Funcțiile date
def xn1_n2_1(n1, n2):
    return np.sin(2 * np.pi * n1 + 3 * np.pi * n2)

def xn1_n2_2(n1, n2):
    return np.sin(4 * np.pi * n1) + np.cos(6 * np.pi * n2)

def Y(n1, n2):
    if n2 == 5 or n2 == N2 - 5:
        return 1
    elif n1 == 5 or n1 == N1 - 5:
        return 1
    elif n1 == 5 and n2 == 5:
        return 1
    else:
        return 0

# Dimensiuni ale imaginii
N1, N2 = 50, 50

# Generare coordonate n1, n2
n1 = np.arange(0, N1)
n2 = np.arange(0, N2)
n1, n2 = np.meshgrid(n1, n2)

# Calcul transformate Fourier
X1 = np.fft.fft2(xn1_n2_1(n1, n2))
X2 = np.fft.fft2(xn1_n2_2(n1, n2))
X3 = np.fft.fft2(np.fromfunction(np.vectorize(Y), (N1, N2)))

# Afișare imaginile și spectrele
plt.figure(figsize=(15, 5))

# Imagini
plt.subplot(231)
plt.imshow(np.abs(xn1_n2_1(n1, n2)), cmap=plt.cm.gray)
plt.title('Imaginea 1')

plt.subplot(232)
plt.imshow(np.abs(xn1_n2_2(n1, n2)), cmap=plt.cm.gray)
plt.title('Imaginea 2')

plt.subplot(233)
plt.imshow(np.abs(np.fromfunction(np.vectorize(Y), (N1, N2))), cmap=plt.cm.gray)
plt.title('Imaginea 3')
var = np.abs(np.fromfunction(np.vectorize(Y), (N1, N2)))
print(var[1:10,1:10])

# Spectre logaritmice
plt.subplot(234)
plt.imshow(np.log1p(np.fft.fftshift(np.abs(X1))), cmap=plt.cm.gray)
plt.title('Spectrul 1')

plt.subplot(235)
plt.imshow(np.log1p(np.fft.fftshift(np.abs(X2))), cmap=plt.cm.gray)
plt.title('Spectrul 2')

plt.subplot(236)
plt.imshow(np.log1p(np.fft.fftshift(np.abs(X3))), cmap=plt.cm.gray)
plt.title('Spectrul 3 (logaritmic)')




plt.tight_layout()
plt.show()








#
# from scipy import fftpack, misc
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Încărcați o imagine de la setul de date
# X = misc.face(gray=True)
#
# # Afișați imaginea originală
# plt.imshow(X, cmap=plt.cm.gray)
# plt.title('Imaginea originală')
# plt.show()
#
# # Aplică transformata Fourier bidimensională
# X_transformed = fftpack.fft2(X)
#
# # Calculează spectrul imaginii
# magnitude_spectrum = np.abs(X_transformed)
#
# # Identifică pragul SNR autoimpus (poate fi ales experimental)
# SNR_threshold = 2  # Poate fi ajustat
#
# # Calculează zgomotul
# noise = np.random.normal(0, 1, size=magnitude_spectrum.shape)
#
# # Calculează SNR
# SNR = 20 * np.log10(np.max(magnitude_spectrum) / np.max(noise))
#
# # Atenuarea în funcție de pragul SNR
# magnitude_spectrum_filtered = np.where(magnitude_spectrum > SNR_threshold, magnitude_spectrum, 0)
#
# # Aplică inversa transformata Fourier bidimensională pentru a obține imaginea comprimată
# X_compressed = np.real(fftpack.ifft2(X_transformed * (magnitude_spectrum_filtered / magnitude_spectrum)))
#
# # Afișează spectrul
# plt.figure(figsize=(8, 8))
#
# plt.subplot(121)
# plt.imshow(np.log(1 + np.fft.fftshift(magnitude_spectrum)), cmap='gray')
# plt.title('Spectrul original')
#
# plt.subplot(122)
# plt.imshow(np.log(1 + np.fft.fftshift(magnitude_spectrum_filtered)), cmap='gray')
# plt.title(f'Spectrul filtrat (SNR={SNR:.2f} dB)')
#
# plt.show()
#
# # Afișează imaginea originală și imaginea comprimată
# plt.figure(figsize=(12, 6))
#
# plt.subplot(1, 2, 1)
# plt.imshow(X, cmap=plt.cm.gray)
# plt.title('Imaginea originală')
#
# plt.subplot(1, 2, 2)
# plt.imshow(X_compressed, cmap=plt.cm.gray)
# plt.title(f'Imaginea comprimată (SNR={SNR:.2f} dB)')
#
# plt.show()



