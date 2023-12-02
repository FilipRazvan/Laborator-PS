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

