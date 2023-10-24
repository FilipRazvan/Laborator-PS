import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt



time_axis_a = np.linspace(0, 4, 44100 * 4)
y_axis_a = np.sin(2 * np.pi * 600 * time_axis_a)
y_axis_b = np.sin(2 * np.pi * 900 * time_axis_a)
y_axis_final = [*y_axis_a, *y_axis_b]

sd.play(y_axis_final, 44100)
sd.wait()

# Observ ca sunetul se modifica atunci cand se ajunge la partea a doua