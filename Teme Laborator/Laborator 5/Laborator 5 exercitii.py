# # A)
# import numpy as np
# import pandas as pd
#
file_path = r'D:\Facultate\anul 4\ps\Train.csv'
#
# # Citim datele si gestionam coloana de datetimes
#
# # data = pd.read_csv(file_path, parse_dates=['Datetime'])
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# # Sortam valorile datetime
# data = data.sort_values(by='Datetime')
#
# # Calculam diferenta si convertim la secunde
# time_differences = np.diff(data['Datetime'].astype(np.int64) // 10**9)  # Convertim la secunde
#
# # eliminam frecventele care sunt 0
# time_differences = time_differences[time_differences > 0]
#
# # Verificam daca exista diferente de timp valabile
# if len(time_differences) > 0:
#     # Calculam frecventa de esantionare pentru timp
#     Fs = 1 / np.mean(time_differences)
#     print(f"Frecventa de esantionare estimata este: {Fs} Hz")
# else:
#     print("Err.")








# # B)
# import pandas as pd
#
# # Preluam datele din fisier
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# # Sortam valorile datetime
# data = data.sort_values(by='Datetime')
#
# # Determinam prima si ultima data
# first_date = data['Datetime'].iloc[0]
# last_date = data['Datetime'].iloc[-1]
#
# # calcul interval timp
# time_interval = last_date - first_date
#
# print(f"Intervalul de timp acoperit de esantioane este: {time_interval}")








# # c ??? afiseaza 0 hz ceva nu iese ok )
# import numpy as np
# import pandas as pd
#
#
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
# # print(data.head())
# # print(data.dtypes)
#
# # Sort pe datetime
# data = data.sort_values(by='Datetime')
#
# # Luam coloana 'Count' pentru a reprezenta semnalul
# signal = data['Count']
#
# # Calculam transformata Fourier a semnalului
# N = len(signal)
# X = np.fft.fft(signal)
#
# # Calculam spectrul de frecventa
# frequencies = np.fft.fftfreq(N)
#
# # cautam si gasim frecventa max
# positive_frequencies = frequencies[:N//2]
# max_frequency_index = np.argmax(np.abs(X[:N//2]))
#
# # Afisam frecv max
# max_frequency = positive_frequencies[max_frequency_index]
# print(f"Frecventa maxima in semnal este: {max_frequency} Hz")


# # c) nu cred ca se afiseaza corect
# import pandas as pd
#
# data = pd.read_csv(file_path, parse_dates=['Datetime'])
#
# time_diff = data['Datetime'].diff()
#
# sampling_rate = 1 / time_diff.mean().total_seconds()
#
# print(f"Frecventa maxima in semnal este: {sampling_rate} Hz")







# # D)
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# # Luam date pentru analiza fourier
# x = data['Count'].values  # Semnalul
#
# transformata = np.fft.fft(x)
#
# # Afișăm graficul modulului transformatei Fourier
# frecvente = np.fft.fftfreq(len(x))
# plt.plot(frecvente, np.abs(transformata))
# plt.xlabel('Frecventa (Hz)')
# plt.ylabel('Modulul Transformatei Fourier')
# plt.title('Transformata Fourier a Semnalului')
# plt.show()













# # E) nu sunt sigur ca afiseaza bine
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# # # Luam datele
# x = data['Count'].values  # Semnalul
#
# transformata = np.fft.fft(x)
#
# # Determinam frecventele corespunzatoare
# frecvente = np.fft.fftfreq(len(x))
#
# # Identificam componenta continua (DC) in spectru
# componenta_continua = np.mean(x)
#
# # Eliminam componenta continua
# transformata[frecvente == 0] = 0
#
# semnal_filtrat = np.fft.ifft(transformata)
#
# plt.plot(data['Datetime'], semnal_filtrat.real)
# plt.xlabel('Timp')
# plt.ylabel('Count')
# plt.title('Semnal fara Componenta Continua')
# plt.show()











# # G)
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# data = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# # # # Luam datele
# x = data['Count'].values  # Semnalul
#
# transformata = np.fft.fft(x)
#
# frecvente = np.fft.fftfreq(len(x))
#
# # Identificam cele mai mari 4 valori ale modulului transformatei
# indici_max = np.argsort(np.abs(transformata))[-4:]
#
# # Afișam frecventele si fenomenele periodice asociate
# for index in indici_max:
#     frecventa = frecvente[index]
#     fenomen_periodic = frecventa if frecventa >= 0 else 1 + frecventa  # pentru frecventele negative
#     valoare_transformata = transformata[index]
#
#     print()
#     print(f"Frecventa: {frecventa} Hz, Modul transformatei: {np.abs(valoare_transformata)}")
#     print(f"Fenomen periodic asociat: {fenomen_periodic} Hz")
#     print("---")



















# # I) dar nu functioneaza filtrarea
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.fft import fft, ifft
#
# semnal = pd.read_csv(file_path, parse_dates=['Datetime'], dayfirst=True)
#
# transformata = fft(semnal['Count'])
#
# # Obtinem frecventa de esantionare
# Fs = 1 / (semnal['Datetime'].iloc[1] - semnal['Datetime'].iloc[0]).total_seconds()
#
# # Obtinem axa frecventelor
# frecvente = np.fft.fftfreq(len(semnal), d=1/Fs)
#
# # Alegem o frecventa de taiere (cat de multe componente de frecventa inalta eliminam)
# frecventa_taiere = 0.1  # taiem toate frecvențele mai mari de 0.1 Hz
#
# # Setam la zero componentele de frecventa inalta
# transformata[np.abs(frecvente) > frecventa_taiere] = 0
#
# # Calculam inversa transformatei Fourier pentru a obtine semnalul filtrat
# semnal_filtrat = ifft(transformata)
#
#
# plt.figure(figsize=(10, 6))
# # Semnalul original
# plt.subplot(2, 1, 1)
# plt.plot(semnal['Datetime'], semnal['Count'])
# plt.title('Semnal Original')
# plt.xlabel('Timp')
# plt.ylabel('Valoare')
#
# # Semnalul filtrat
# plt.subplot(2, 1, 2)
# plt.plot(semnal['Datetime'], semnal_filtrat.real)  # .real pentru a ignora partea imaginara
# plt.title('Semnal Filtrat')
# plt.xlabel('Timp')
# plt.ylabel('Valoare')
#
# plt.tight_layout()
# plt.show()

