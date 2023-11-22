import numpy as np
# Generam aleator coeficientii ptr cele 2 polinoame
# Generarea aleatoare a coeficienților pentru cele două polinoame
N = 5
p_coefficients = np.random.randint(-10, 10, size=N + 1)
q_coefficients = np.random.randint(-10, 10, size=N + 1)

# definim polinoamele
p = np.poly1d(p_coefficients)
q = np.poly1d(q_coefficients)

# produs folosind np.convolve
convolution_result_direct = np.convolve(p_coefficients, q_coefficients, mode='full')

# Este necesar sa ajustam dimensiunea pentru a obtine un rez corect cu FFT
new_size = len(p_coefficients) + len(q_coefficients) - 1
p_fft = np.fft.fft(p_coefficients, new_size)
q_fft = np.fft.fft(q_coefficients, new_size)
fft_result = np.fft.ifft(p_fft * q_fft).real


print("Coeficientii polinomului p(x):", p_coefficients)
print("Coeficientii polinomului q(x):", q_coefficients)
print("Rezultatul convoluției directe:", convolution_result_direct)
print("Rezultatul convoluției folosind fft:", np.rint(fft_result).astype(int))
