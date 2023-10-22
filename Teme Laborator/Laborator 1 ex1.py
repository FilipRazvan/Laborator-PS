# Tema 1
# Exercitiul 1
# a)

# import numpy as np
# import matplotlib.pyplot as plt
#
# t = np.arange(0, 0.03, 0.0005)
# # Luam un vector t de la 0 la 0.03 si il discretizam cu un pas de 0.0005
#
# x = np.cos(520 * np.pi * t + np.pi / 3)
# y = np.cos(280 * np.pi * t - np.pi / 3)
# z = np.cos(120 * np.pi * t + np.pi / 3)
# # Avem semnalele continue din cerinta
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, x, label='x(t)')
# plt.plot(t, y, label='y(t)')
# plt.plot(t, z, label='z(t)')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.title('Semnalele continue x(t), y(t) si z(t)')
# plt.legend()
# plt.grid(True)
# plt.show()


# Tema 1
# Exercitiul 1
# b)

# import numpy as np
# import matplotlib.pyplot as plt
#
# fs = 2000
# # Am ales frecventa de esantionare de 2000HZ
#
# t = np.arange(0, 0.03, 1/fs)
# # Am luat un vector t de la 0 la 0.03 cu discretizarea 1/2000
#
# # Definirea semnalelor eșantionate
# x_n = np.cos(520 * np.pi * t + np.pi / 3)
# y_n = np.cos(280 * np.pi * t - np.pi / 3)
# z_n = np.cos(120 * np.pi * t + np.pi / 3)
#
# # Crearea subgraficelor
# plt.figure(figsize=(10, 6))
#
# # Subgrafic pentru x[n]
# plt.subplot(311)
# plt.plot(t, x_n)
# plt.title('Semnal x[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
# # Subgrafic pentru y[n]
# plt.subplot(312)
# plt.plot(t, y_n)
# plt.title('Semnal y[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
# # Subgrafic pentru z[n]
# plt.subplot(313)
# plt.plot(t, z_n)
# plt.title('Semnal z[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
# # Afișarea subgraficelor
# plt.tight_layout()
# plt.show()


# Tema 1
# Exercitiul 1
# c)

# import numpy as np
# import matplotlib.pyplot as plt
#
# t = np.arange(0, 0.03, 0.0005)
#
# x = np.cos(520 * np.pi * t + np.pi / 3)
# y = np.cos(280 * np.pi * t - np.pi / 3)
# z = np.cos(120 * np.pi * t + np.pi / 3)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, x, label='x(t)')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.title('Semnal continuu x(t)')
# plt.legend()
# plt.grid(True)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, y, label='y(t)')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.title('Semnal continuu y(t)')
# plt.legend()
# plt.grid(True)
#
# plt.figure(figsize=(10, 6))
# plt.plot(t, z, label='z(t)')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.title('Semnal continuu z(t)')
# plt.legend()
# plt.grid(True)
#
# plt.show()

###############################################



# import numpy as np
# import matplotlib.pyplot as plt
#
#
# t = np.arange(0, 1, 1/6)
#
# x_n = np.cos(520 * np.pi * t + np.pi / 3)
# y_n = np.cos(280 * np.pi * t - np.pi / 3)
# z_n = np.cos(120 * np.pi * t + np.pi / 3)
#
# plt.figure(figsize=(10, 6))
#
# plt.subplot(311)
# plt.plot(t, x_n)
# plt.title('Semnal x[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
# plt.subplot(312)
# plt.plot(t, y_n)
# plt.title('Semnal y[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
# plt.subplot(313)
# plt.plot(t, z_n)
# plt.title('Semnal z[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
#
#
# plt.tight_layout()
# plt.show()








# import numpy as np
# import matplotlib.pyplot as plt
#
# t_discret = np.arange(0, 1, 1/6)
# t_continuu = np.arange(0, 1, 1/6)
#
# x_discret = np.cos(520 * np.pi * t_discret + np.pi / 3)
# x_continuu = np.cos(520 * np.pi * t_continuu + np.pi / 3)
#
# y_discret = np.cos(280 * np.pi * t_discret - np.pi / 3)
# y_continuu = np.cos(280 * np.pi * t_continuu - np.pi / 3)
#
#
# z_discret = np.cos(120 * np.pi * t_discret + np.pi / 3)
# z_continuu = np.cos(120 * np.pi * t_continuu + np.pi / 3)
#
# plt.figure(figsize=(10, 6))
#
# plt.plot(t_continuu, x_continuu, label='x(t)', color='blue')
# plt.stem(t_discret, x_discret, basefmt=' ', linefmt='r-', markerfmt='ro', label='x[n]')
# plt.title('Semnal continuu x(t) și Semnal discret x[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.legend()
# plt.grid(True)
#
#
# plt.figure(figsize=(10, 6))
# plt.plot(t_continuu, y_continuu, label='y(t)', color='yellow')
# plt.stem(t_discret, y_discret, basefmt=' ', linefmt='r-', markerfmt='ro', label='y[n]')
# plt.title('Semnal continuu y(t) și Semnal discret y[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.legend()
# plt.grid(True)
#
#
# plt.figure(figsize=(10, 6))
# plt.plot(t_continuu, z_continuu, label='z(t)', color='green')
# plt.stem(t_discret, z_discret, basefmt=' ', linefmt='r-', markerfmt='ro', label='z[n]')
# plt.title('Semnal continuu z(t) și Semnal discret z[n]')
# plt.xlabel('Timp (s)')
# plt.ylabel('Amplitudine')
# plt.legend()
# plt.grid(True)
#
# plt.show()