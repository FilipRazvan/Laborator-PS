import numpy as np
import matplotlib.pyplot as plt

# Funcție pentru a genera polinoame aleatoare cu coeficienți întregi
def generate_random_polynomial(N):
    return np.random.randint(-10, 10, N + 1)

# Funcție pentru a calcula produsul polinoamelor folosind convoluția directă
def convolution_product(p, q):
    return np.convolve(p, q, mode='full')

# Funcție pentru a calcula produsul polinoamelor folosind FFT
def fft_product(p, q):
    fft_p = np.fft.fft(p)
    fft_q = np.fft.fft(q)

    product_fft = fft_p * fft_q
    product = np.fft.ifft(product_fft)

    return np.real(product)

# Gradul maxim al polinoamelor
N = 5

# Generați două polinoame aleatoare
p = generate_random_polynomial(N)
q = generate_random_polynomial(N)

# Calculați produsul folosind convoluția directă
result_convolution = convolution_product(p, q)

# Calculați produsul folosind FFT
result_fft = fft_product(p, q)

# Afișați rezultatele în consolă
print("Polinomul p(x):", p)
print("Polinomul q(x):", q)

print("\nProdusul folosind convoluția directă:", result_convolution)
print("Produsul folosind FFT:", result_fft)

# Afișați rezultatele în grafice
plt.figure(figsize=(15, 10))

# Afișați polinoamele originale
plt.subplot(4, 1, 1)
plt.stem(p, basefmt='b-', linefmt='b-', markerfmt='bo', label='p(x)')
plt.legend()

plt.subplot(4, 1, 2)
plt.stem(q, basefmt='g-', linefmt='g-', markerfmt='go', label='q(x)')
plt.legend()

# Afișați rezultatul convoluției directe
plt.subplot(4, 1, 3)
plt.stem(result_convolution, basefmt='r-', linefmt='r-', markerfmt='ro', label='p(x) * q(x) (Convoluție Directă)')
plt.legend()

# Afișați rezultatul folosind FFT
plt.subplot(4, 1, 4)
plt.stem(result_fft, basefmt='purple', linefmt='purple', markerfmt='p', label='p(x) * q(x) (FFT)')
plt.legend()

plt.tight_layout()
plt.show()
