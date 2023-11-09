# D:\Facultate\anul 4\ps

import numpy as np

file_path = r'D:\Facultate\anul 4\ps\Train.csv'

data = np.genfromtxt(file_path, delimiter=',')

# luam coloana count din data
count_values = data['Count']

# calculam diferenta de timp
time_differences = np.diff(count_values)

# calculam frecventa de esantionare pentru timp
Fs = 1 / np.mean(time_differences)

print(f"Frecvența de eșantionare estimată este: {Fs} Hz")

