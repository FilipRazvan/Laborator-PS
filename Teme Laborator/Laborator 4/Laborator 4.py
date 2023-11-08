import numpy as np
import matplotlib.pyplot as plt
import math
import time


def FourierFunction(w,n):
    X_array = []
    for j in range(w): #  spectrul de frecventa
        xw = 0
        for i in range(len(n)): # Aici calculan datele pentru spectrul de frecventa
            xw += n[i] * math.e ** (-2 * np.pi * 1j * j * i/len(n))
        X_array.append(xw)
    return X_array


timpiExecutieCustom = []
timpiExecutieNumpy = []
N_valori = [128, 256, 512, 1024, 2048, 4096, 8192]

for N in N_valori:
    data = np.arange(N)
    # data = np.random.random(N)
    # print(data)
    # date = np.random.rand(N)  # Generați date aleatoare pentru test


    start_time = time.time()
    _ = FourierFunction(N, data) # Nu atribuim la nimic deoarece nu ne intereseaza rezultatul ci doar timpul
    end_time = time.time()
    timpiExecutieCustom.append(end_time - start_time)

    # start_time = time.time()
    # _ = np.fft.fft(data) # Nu atribuim la nimic deoarece nu ne intereseaza rezultatul ci doar timpul
    # end_time = time.time()
    # timpiExecutieNumpy.append(end_time - start_time)

    start_time2 = time.perf_counter()
    _ = np.fft.fft(data)
    end_time2 = time.perf_counter()
    timpiExecutieNumpy.append(end_time2 - start_time2)

print ("Timp executie custom pentru n=", N ,"este = ", timpiExecutieCustom, "iar timp executie numpy este =", timpiExecutieNumpy)



fig, axs = plt.subplots(2, figsize=(5, 10))

# Subgraficul pentru implementarea personalizată
axs[0].plot(N_valori, timpiExecutieCustom, label='Implementare proprie', marker='o')
axs[0].set_yscale('log')
axs[0].set_xlabel('Dimensiunea vectorului (N)')
axs[0].set_ylabel('Timpul de execuție (secunde)')
axs[0].legend()

# Subgraficul pentru numpy.fft
print(N_valori)
print(timpiExecutieNumpy)
axs[1].plot(N_valori, timpiExecutieNumpy, label='numpy.fft', marker='o')
axs[1].set_yscale('log')
axs[1].set_xscale('log')
axs[1].set_xlabel('Dimensiunea vectorului (N)')
axs[1].set_ylabel('Timpul de execuție (secunde)')
axs[1].legend()


plt.tight_layout()
plt.show()

# plt.plot(N_valori, timpiExecutieCustom, label='Implementare proprie')
# plt.plot(N_valori, timpiExecutieNumpy, label='numpy.fft')
# plt.yscale('log')
# plt.xlabel('Dimensiunea vectorului (N)')
# plt.ylabel('Timpul de execuție (secunde)')
# plt.legend()
# plt.show()

# execution_times_custom, execution_times_numpy = measure_execution_time(N_values)
#
# plt.plot(N_values, execution_times_custom, label='Implementare proprie')
# plt.plot(N_values, execution_times_numpy, label='numpy.fft')
# plt.yscale('log')
# plt.xlabel('Dimensiunea vectorului (N)')
# plt.ylabel('Timpul de execuție (secunde)')
# plt.legend()
# plt.show()