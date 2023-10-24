import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile
import time

fig, axs = plt.subplots(4)
fig.suptitle("Exercitiul 2")
time_axis_a = np.linspace(0, 4, 160)

y_axis_a = np.sin(520 * np.pi * time_axis_a + np.pi / 3)
y_axis_b = np.sin(520 * np.pi * time_axis_a + np.pi / 2)
y_axis_c = np.sin(520 * np.pi * time_axis_a)
y_axis_d = np.sin(520 * np.pi * time_axis_a + 3 * np.pi / 4)

# Generați un vector de zgomot cu aceeași dimensiune ca semnalele
functie = np.random.normal(size=len(time_axis_a))
norma = np.linalg.norm(functie)

norma1 = np.linalg.norm(y_axis_a)
norma2 = np.linalg.norm(y_axis_b)
norma3 = np.linalg.norm(y_axis_c)
norma4 = np.linalg.norm(y_axis_d)

gama1 = np.sqrt(norma1 / (0.1 * norma))
gama2 = np.sqrt(norma2 / (0.1 * norma))
gama3 = np.sqrt(norma3 / (0.1 * norma))
gama4 = np.sqrt(norma4 / (0.1 * norma))

y_axis_a = np.sin(520 * np.pi * time_axis_a + np.pi / 3) + (gama1 * functie)
y_axis_b = np.sin(520 * np.pi * time_axis_a + np.pi / 2) + (gama2 * functie)
y_axis_c = np.sin(520 * np.pi * time_axis_a) + (gama3 * functie)
y_axis_d = np.sin(520 * np.pi * time_axis_a + 3 * np.pi / 4) + (gama4 * functie)

axs[0].plot(time_axis_a, y_axis_a)
axs[0].set_title("Var1")
axs[1].plot(time_axis_a, y_axis_b)
axs[1].set_title("Var2")
axs[2].plot(time_axis_a, y_axis_c)
axs[2].set_title("Var3")
axs[3].plot(time_axis_a, y_axis_d)
axs[3].set_title("Var4")

sd.play(y_axis_a, 16000)
time.sleep(2)
sd.wait()
wavfile.write("semnal_y_axis_a.wav", 16000, y_axis_a)
sample_rate, loaded_signal = wavfile.read("semnal_y_axis_a.wav")


plt.tight_layout()
plt.show()

