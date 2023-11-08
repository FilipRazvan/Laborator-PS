# Ca sa demonstram ca daca alegem o frecventa de esantionare mai mare decat frecventa Nyquist, putem schimba frecventa
# de esantionare pentru a fi mai mare decat Nyquist
# Codul utilizeaza frecventa 20 * f, care este peste Nyquist, pentru semnalul original (f) si se observa ca fenomenul de
# aliasing nu mai este valabil in cazul de fata.
import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului original
f = 2  # Frecventa semnalului original
amplitudine = 1

# Frecventa de esantionare peste Nyquist
frecventa_esantionare = 20 * f  # Peste Nyquist pentru semnalul original

faza_semnal = 0

# Generam semnalul original
t = np.linspace(0, 1, 1000, endpoint=False)  # Axa timpului
semnal_original = amplitudine * np.sin(2 * np.pi * f * t + faza_semnal)

# Eșantionam semnalul original cu frecventa de eșantionare peste Nyquist
timp_esantionare = np.arange(0, 1, 1/frecventa_esantionare)
semnal_esantionat = amplitudine * np.sin(2 * np.pi * f * timp_esantionare + faza_semnal)

# Facem alte 2 semnale care vor produce aceleași eșantioane ca semnalul original
frecventa1 = frecventa_esantionare + 3 * f
frecventa2 = frecventa_esantionare + 2.5 * f

semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * t + faza_semnal)
semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * t + faza_semnal)

# Afișare semnale
plt.figure(figsize=(14, 8))

plt.plot(t, semnal_original, label='Semnal original')
plt.plot(t, semnal1, label='Semnal 1')
plt.plot(t, semnal2, label='Semnal 2')

# Eșantioane semnal original
plt.plot(timp_esantionare, semnal_esantionat, 'o', label='Eșantioane')

plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Demonstrarea efectului de eșantionare peste Nyquist')
plt.legend()
plt.grid(True)
plt.savefig("L4ex3.pdf")
plt.savefig("L4ex3.png")
plt.show()