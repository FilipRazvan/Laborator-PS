import numpy as np
import matplotlib.pyplot as plt

fs = 44100
# Folosinm rata de esantionare standard pentru sunet audio CD

# A)   f = 1/T =>  T = 1/f
T_a = 1 / (fs / 2)

# B)
T_b = 1 / (fs / 4)

# C)
# f = 0hz, deoarece T_c este infinita. Semnalul nu se schimba

time_axis_a = np.linspace(0, T_a, int(fs * T_a))

time_axis_b = np.linspace(0, T_b, int(fs * T_b))

y_axis_a = np.sin(2 * np.pi * (fs / 2) * time_axis_a)
y_axis_b = np.sin(2 * np.pi * (fs / 4) * time_axis_b)

y_axis_c = np.ones_like(time_axis_a)

plt.figure(figsize=(12, 6))

plt.subplot(311)
plt.plot(time_axis_a, y_axis_a)
plt.title("f = fs/2")

plt.subplot(312)
plt.plot(time_axis_b, y_axis_b)
plt.title("f = fs/4")

plt.subplot(313)
plt.plot(time_axis_a, y_axis_c)
plt.title("f = 0 Hz")

plt.tight_layout()
plt.show()


# Observam ca ptr f = fs/2 semnalul are o frecventa de jum de frecventa de esantionare, deci are un ciclu complet in fiecare secunda.

# Pentru f = fs/4 are frecventa cat un sfert din frecventa de esantionare, are un ciclu complet la 4 secunde, deci se aude mai incet putin ca si cel de sus
# pentru f = 0 hz, este constant, nu are variatii in timp deci nu se aude nimic