import numpy as np
import matplotlib.pyplot as plt

N = 8

# Generare matrice fourier
F = np.fft.fft(np.eye(N))

# Calcularea matricei fourier ortogonale
F_ortogonal = np.conj(F.T) / N

# Verificarea ortogonalitații
is_orthogonal = np.allclose(np.dot(F, F_ortogonal), np.eye(N))

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('Matrice fourier N=8')

# reala
axes[0, 0].imshow(np.real(F), cmap='jet')
axes[0, 0].set_title('Partea reala a matricei fourier')
axes[0, 0].axis('off')

# imaginara
axes[0, 1].imshow(np.imag(F), cmap='jet')
axes[0, 1].set_title('Partea imaginara a matricei fourier')
axes[0, 1].axis('off')

# parte reala a matricei ortogonale
axes[1, 0].imshow(np.real(F_ortogonal), cmap='jet')
axes[1, 0].set_title('Partea reala a matricei fourier ortogonale')
axes[1, 0].axis('off')

# parte imaginara a matricei ortogonale
axes[1, 1].imshow(np.imag(F_ortogonal), cmap='jet')
axes[1, 1].set_title('Partea imaginara a matricei fourier ortogonale')
axes[1, 1].axis('off')

plt.show()

# verificam daca este ortogonala
if is_orthogonal:
    print("Matricea este ortogonala.")
else:
    print("Matricea NU este ortogonala.")
