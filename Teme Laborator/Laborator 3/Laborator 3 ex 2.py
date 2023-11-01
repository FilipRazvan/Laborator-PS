import numpy as np
import matplotlib.pyplot as plt
import math


def FourierFunction(t,w):
    return math.e ** (-2 * np.pi * 1j * t * w)

sin_function = lambda x: np.sin(2 * np.pi * 13 * x)
# Functie sinusoidala care este data de un sinus cu frecventa 13hz

fig, axs = plt.subplots(6, figsize=(5, 10))
fig.suptitle("Exercitiul 2")
time_axis = np.linspace(0, 1, 1000)
y_axis = sin_function(time_axis)

axs[0].plot(time_axis, y_axis)
axs[0].set_title("Fig 1.1")


fourier_a = FourierFunction(time_axis, 1)
axs[1].plot(y_axis * fourier_a.real, y_axis * fourier_a.imag)
axs[1].set_title("Fig 1.2 si 2.1")


fourier_b = FourierFunction(time_axis, 2)
axs[2].plot(y_axis * fourier_b.real, y_axis * fourier_b.imag)
axs[2].set_title("Fig 2.1")


fourier_c = FourierFunction(time_axis, 5)
axs[3].plot(y_axis * fourier_c.real, y_axis * fourier_c.imag)
axs[3].set_title("Fig 2.2")


fourier_d = FourierFunction(time_axis, 7)
axs[4].plot(y_axis * fourier_d.real, y_axis * fourier_d.imag)
axs[4].set_title("Fig 2.3")


fourier_e = FourierFunction(time_axis, 13)
axs[5].plot(y_axis * fourier_e.real, y_axis * fourier_e.imag)
axs[5].set_title("Fig 2.4")
plt.savefig("ex2.pdf")
plt.savefig("ex2.png")


plt.tight_layout()
plt.show()
