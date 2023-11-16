import numpy as np
import matplotlib.pyplot as plt

# luam un vector aleator
N = 100
x = np.random.rand(N)

plt.figure(figsize=(15, 10))

plt.subplot(4, 1, 1)
plt.plot(x)
plt.title('x[n] initial')

plt.subplot(4, 1, 2)
x_squared = np.convolve(x, x, mode='full')
plt.plot(x_squared)
plt.title('x * x (prima convolutie)')

plt.subplot(4, 1, 3)
x_cubed = np.convolve(x_squared, x, mode='full')
plt.plot(x_cubed)
plt.title('x * x * x (a doua convolutie)')

plt.subplot(4, 1, 4)
x_last = np.convolve(x_cubed, x,mode='full')
plt.plot(x_last)
plt.title('x * x * x (gaussiana)')

plt.tight_layout()
plt.show()
