import numpy as np
import matplotlib.pyplot as plt

# Aleg functia sin (t) = sin pi/2 + pi/2
amplitudine = 1.0
frecventa = 1.0
faza = np.pi/2

durata = 1.0 # Am ales durata 1 secunda
frecventa_esantionare = 1000  # am ales 1000hz frecventa

timp = np.linspace(0, durata, int(durata * frecventa_esantionare), endpoint=False)

semnalCosinus = amplitudine * np.sin( 2* np.pi * frecventa * timp )

semnalSinus = amplitudine * np.sin( 2* np.pi * frecventa * timp +faza - np.pi/2 )

#semnalSinus = amplitudine * np.sin(2* np.pi * frecventa * timp + faza - np.pi/2)

plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(timp, semnalSinus)
plt.title('Semnal Sinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(timp, semnalCosinus)
plt.title('Semnal Cosinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid()

plt.tight_layout()
plt.show()