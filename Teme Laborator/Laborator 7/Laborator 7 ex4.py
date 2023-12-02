import numpy as np
import matplotlib.pyplot as plt

Fs = 1000 # Frecvența de eșantionare
t = np.arange(0, 5, 1/Fs)  # Timpul de la 0 la 5 secunde
f1 = 50  # Frecvența primului instrument
f2 = 200  # Frecvența celui de-al doilea instrument

# Semnalul audio combinat cu cele 2 instrumente
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# semnal original afisare
plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Semnalul original')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')

# eliminam frecventa instrum ales
frecventa_instrument_eliminate = f1
signal_filtrat = signal - np.sin(2 * np.pi * frecventa_instrument_eliminate * t)

# afisare semnal fara instrument
plt.subplot(2, 1, 2)
plt.plot(t, signal_filtrat)
plt.title('Semnal fara Instrument')
plt.xlabel('Timp')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
