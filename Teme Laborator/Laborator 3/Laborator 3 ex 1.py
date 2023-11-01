import numpy as np
import matplotlib.pyplot as plt

# Conform cerintei, n = 8
N = 8


F = np.zeros((N, N), dtype=complex)
for n in range(N):
    for omega in range(N):
        F[n, omega] = np.exp(-2 * np.pi * 1j * n * omega / N) / np.sqrt(N)
        # Am impartit la radacina patrata a dimensiunii pentru a asigura unitaritatea, altfel nu ar fi dat true

# Calculam transpusa conjugata  si ar trebui sa ne dea o matrice care este un multiplu al matricei identitate
F_H = np.conjugate(F).T

# Verificam daca F * F_H este un multiplu al matricei identitate
result = np.dot(F, F_H)
unitaraBool = np.allclose(result, np.eye(N))

print("Este F unitara?", unitaraBool)



# # Separam partea reala de cea imaginara:
parte_reala = np.real(F)
parte_imaginara = np.imag(F)

#  cream axa timp
n = np.arange(N)

for i in range(N):
    plt.subplot(N, 2, 2 * i + 1)
    plt.plot(n, parte_reala[i])
    plt.title(f"parte reala - Linia {i + 1}")

    plt.subplot(N, 2, 2 * i + 2)
    plt.plot(n, parte_imaginara[i])
    plt.title(f"parte imaginara - Linia {i + 1}")

plt.savefig("ex1.pdf")
plt.savefig("ex1.png")

plt.tight_layout()

plt.show()





# # Separam partea reala de cea imaginara:
# parte_reala = np.real(F)
# partea_imaginara = np.imag(F)
#
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.imshow(parte_reala, cmap='RdBu', aspect='auto')
# plt.title("Parte reala")
# plt.colorbar()
#
#
#
# plt.subplot(1, 2, 2)
# plt.imshow(partea_imaginara, cmap='RdBu', aspect='auto')
# plt.title("Parte Imaginara")
# plt.colorbar()
#
# plt.show()