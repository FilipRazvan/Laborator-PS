import numpy as np
import matplotlib.pyplot as plt

def rectangular(n):
    return np.ones(n)

def hanning(n):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(n) / n))

t = np.linspace(0, 1, 200)
x = np.sin(2 * np.pi * 100 * t)

hanningWindow = hanning(200)
xWithHanning = x * hanningWindow

rectangularWindow = rectangular(200)
xWithRectangular = x * rectangularWindow

fig, axs = plt.subplots(2, sharex=True)

# axs[0].set_title("Original")
# axs[0].plot(t, x)

axs[0].set_title("Rectangular")
axs[0].plot(t, xWithRectangular)

axs[1].set_title("Hanning")
axs[1].plot(t, xWithHanning)

# Adăugarea etichetelor și legendei
axs[1].set_xlabel("Time")
for ax in axs:
    ax.set_ylabel("Amplitude")

# axs[0].legend(["Original"])
axs[0].legend(["Rectangular"])
axs[1].legend(["Hanning"])

plt.show()
