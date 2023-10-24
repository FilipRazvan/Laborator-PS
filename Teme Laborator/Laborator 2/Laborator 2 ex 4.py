import numpy as np
import matplotlib.pyplot as plt

# a
fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 4")
time_axis_a = np.linspace(0, 4, 1600)
y_axis_a = np.sin(2 * np.pi * time_axis_a)
axs[0].plot(time_axis_a, y_axis_a)
axs[0].set_title("Sinusoidala")
# c
sawtooth_function = lambda x: x % 1
y_axis_c = sawtooth_function(time_axis_a)
axs[1].plot(time_axis_a, y_axis_c)
axs[1].set_title("Sawtooth")

y_axis_sum = np.add(y_axis_c,y_axis_a)

axs[2].plot(time_axis_a, y_axis_sum)
axs[2].set_title("Sum")

plt.tight_layout()
plt.show()
