# Laborator 1
# ex 2
# a)

import numpy as np
import matplotlib.pyplot as plt

# frecventa = 400
#
#
# # Intervalul de timp
# t = np.linspace(0, 4, 1600)
#
# semnalSinusoidal = np.sin(2 * np.pi * frecventa * t)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, semnalSinusoidal)
# plt.title('Semnal Sinusoidal de 400 Hz')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.grid(True)


# b)

# frecventa = 400
# durata = 3
#
# t = np.linspace(0, durata, durata*frecventa)
#
# semnalSinusoidal = np.sin(2 * np.pi * frecventa * t)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, semnalSinusoidal)
# plt.title('Semnal Sinusoidal de 800 Hz care dureaza 3 secunde')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.grid(True)
#
# plt.show()




# C)
# from scipy.signal import sawtooth
#
# frecventa = 240
# durata = 3
#
# t = np.linspace(0, durata, frecventa*durata)
#
# semnalSawTooth = sawtooth(2 * np.pi * frecventa * t)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, semnalSawTooth)
# plt.title('Semnal "Sawtooth" de 240 Hz')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.grid(True)
# plt.show()




# D)

# frecventa = 300
#
# t = np.linspace(0, 1, 1000)
#
# semnalSign = np.sign(np.sin(2 * np.pi * frecventa * t))
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, semnalSign)
# plt.title('Semnal de tip "Square" de 300 Hz')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.grid(True)
# plt.show()





# E)
# x = 128    # linii
# y = 128    # coloane
#
# semnalAleator = np.random.rand(x, y)
#
# # Afișăm semnalul generat folosind imshow
# plt.imshow(semnalAleator, cmap='viridis')
# plt.title('Semnal 2D Aleator')
# plt.colorbar()
# plt.show()





# F)

x = 128
y = 128

semnal2D = np.zeros((x, y))  # vector cu toate elementele zero

numar_dungi_pare = 4

inaltime_dunga = x // numar_dungi_pare
# Folosim // ca rezultatul sa dea mereu un nr intreg

for i in range(numar_dungi_pare):
    if i % 2 == 0:
        semnal2D[i*inaltime_dunga:(i+1)*inaltime_dunga, :] = 1

plt.imshow(semnal2D, cmap='gray')
plt.title('Imagine cu dungi orizontale')
plt.axis('off')
plt.show()

