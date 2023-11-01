import numpy as np
import matplotlib.pyplot as plt
import math

frecventa1 = 3
frecventa2 = 7
frecventa3 = 87

fig, axs = plt.subplots(2)
fig.suptitle("Exercitiul 3")
time_axis = np.linspace(0, 1, 1000)
y_axis = np.sin(2 * np.pi * frecventa1 * time_axis) + np.sin(2 * np.pi * frecventa2 * time_axis) + np.sin(2 * np.pi * frecventa3 * time_axis)

def FourierFunction(w,n):
    X_array = []
    for j in range(w):
        xw = 0
        for i in range(len(n)):
            xw += n[i] * math.e ** (-2 * np.pi * 1j * j * i/len(n))
        X_array.append(xw)
    return X_array


absFourier = np.abs(FourierFunction(100, y_axis))
# Calculeaza trans fourier a semnalului y pentru 100 de frecvente diferite. Se vor calcula in total 100 puncte in spectrul de frecv al transf Fourier.Folosim abs pentru a calcula valoarea absoluta a valorii
axs[0].plot(time_axis, y_axis)
axs[0].set_title("Fig 2.1")

axs[1].plot(absFourier)
axs[1].set_title("Fig 2.2")

plt.tight_layout()
plt.show()

plt.savefig("ex3.pdf")
plt.savefig("ex3.png")
