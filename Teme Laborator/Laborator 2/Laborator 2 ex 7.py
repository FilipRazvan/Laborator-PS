import numpy as np
import matplotlib.pyplot as plt

f_initial = 1000 # Frecventa initiala

T_initial = 1 / f_initial # timpul initial

time_axis_initial = np.linspace(0, 1, int(f_initial))
y_axis_initial = np.sin(2 * np.pi * f_initial * time_axis_initial)

y_decimated = y_axis_initial[::4]
# decimam semnalul, pastram doar fiecare al 4-lea element
time_axis_decimated = np.linspace(0, 1, len(y_decimated))

plt.figure(figsize=(12, 6))

plt.subplot(211)
plt.plot(time_axis_initial, y_axis_initial)
plt.title("Semnal initial")

plt.subplot(212)
plt.plot(time_axis_decimated, y_decimated)
plt.title("Semnal decimat")

# plt.tight_layout()
# plt.show()


# B)

y_decimated_from_second = y_axis_initial[1::4]
time_axis_decimated_from_second = np.linspace(0, 1, len(y_decimated_from_second))
# Am decimat si am pastrat doar al patrulea element pornind cu elementul 2

plt.figure(figsize=(6, 3))
plt.plot(time_axis_decimated_from_second, y_decimated_from_second)
plt.title("Semnal decimat de la al doilea element")
plt.show()


# In primul caz, am decimat la 250hz si am pastrat doar al patrulea esantion, frecventa este de 4 ori mai mica insa forma este foarte asemanatoare

# In cazul 2, am pornit de la al doilea element al semnalului initial. Am decimat semnalul la 250hz dar am inceput de la al doilea esantion si rezultatul este diferit.
