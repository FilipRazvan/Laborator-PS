
import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului original
f = 2  # Frecventa semnalului original
amplitudine = 1
# frecventa_esantionare = 15  # Frecventa de esantionare (sub-Nyquist)

# Frecvența de esanționare sub-Nyquist
frecventa_esantionare = 2 * f  # Sub-Nyquist pentru semnalul original

faza_semnal = 0

# Generam semnalul original
t = np.linspace(0, 1, 1000, endpoint=False)  # axa Timp
semnal_original = amplitudine * np.sin(2 * np.pi * f * t + faza_semnal)


# Esantionam semnalul original cu frecventa de esantionare
timp_esantionare = np.arange(0, 1, 1/frecventa_esantionare)
semnal_esantionat = amplitudine * np.sin(2 * np.pi * f * timp_esantionare + faza_semnal)


# Facem alte 2 semnale care vor produce aceleasi esantioane ca semnalul initial
frecventa1 = frecventa_esantionare + 0.5 * frecventa_esantionare
frecventa2 = frecventa_esantionare + 1.5 * frecventa_esantionare


semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * t + faza_semnal)
semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * t + faza_semnal)


# Afișare semnale
plt.figure(figsize=(14, 8))

plt.plot(t, semnal_original, label='semnal original')

# Afisare semnale
plt.plot(t, semnal1, label='Semnal 1')
plt.plot(t, semnal2, label='Semnal 2')

# Esanțioane semnal original
plt.plot(timp_esantionare, semnal_esantionat, 'o', label='Esanțioane')

plt.xlabel('Timp')
plt.ylabel('Amplitudine')
plt.title('Demonstrarea fenomenului de aliasing')
plt.legend()
plt.grid(True)
plt.savefig("L4ex2.pdf")
plt.savefig("L4ex2.png")
plt.show()
