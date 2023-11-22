import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy

data = pd.read_csv("Train.csv")[24*7:24*10]
dataCount = data['Count']
time_axis = np.linspace(0, 72, 72)
fig, axs = plt.subplots(3)
fig.suptitle("Exercitiul 2")
axs[0].plot(time_axis, dataCount)
axs[0].set_title("Nr masini fiecare ora")
w_values = [11, 17, 23, 29]

convolves = []
for value in w_values:
    convolves.append(np.convolve(dataCount, np.ones(value), 'valid'))

# c
frecv_taiere = 1/4
print(f"Frecventa este de {1 / 3600}Hz, iar eu voi alege o frecventa de taiere de {1/(3600 * 4)}Hz, pentru a evita fluctuatii mari ale semnalului")


# d

butter = scipy.signal.butter(5, frecv_taiere)
cheby1 = scipy.signal.cheby1(5, 5, frecv_taiere)


# e
filteredButter = scipy.signal.filtfilt(butter[0], butter[1], dataCount)
filteredCheby1 = scipy.signal.filtfilt(cheby1[0], cheby1[1], dataCount)
axs[1].plot(filteredButter)
axs[1].set_title("Mesaj filtrat butter")
axs[2].plot(filteredCheby1)
axs[2].set_title("Mesaj filtrat cheby")
# Voi alege cheby pentru ca este mai eficient in a "rejecta" noise-ul
plt.show()

# f
fig2, axs2 = plt.subplots(3)
fig2.suptitle("Subpunctul f")

butter = scipy.signal.butter(2, frecv_taiere)
cheby1 = scipy.signal.cheby1(4, 6, frecv_taiere)
cheby12 = scipy.signal.cheby1(3, 7, frecv_taiere)
filteredButter = scipy.signal.filtfilt(butter[0], butter[1], dataCount)
filteredCheby1 = scipy.signal.filtfilt(cheby1[0], cheby1[1], dataCount)
filteredCheby12 = scipy.signal.filtfilt(cheby12[0], cheby12[1], dataCount)
axs2[0].plot(filteredButter)
axs2[0].set_title("Mesaj filtrat butter")
axs2[1].plot(filteredCheby1)
axs2[1].set_title("Mesaj filtrat cheby 1 ")
axs2[2].plot(filteredCheby12)
axs2[2].set_title("Mesaj filtrat cheby 2")


plt.tight_layout()
plt.show()
