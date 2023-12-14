# import numpy as np
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
#
#
#
# N = 1000
# t = np.arange(N)
# trend = 0.02 * t**2 + 0.5 * t + 10
# f1, f2 = 0.1, 0.01
# season = 5 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t)
# noise = np.random.normal(0, 1, N)
# serie_timp = trend + season + noise
#
# plt.figure(figsize=(12, 6))
# plt.subplot(4, 1, 1)
# plt.plot(t, trend, label='Trend')
# plt.legend()
#
# plt.subplot(4, 1, 2)
# plt.plot(t, season, label='Season')
# plt.legend()
#
# plt.subplot(4, 1, 3)
# plt.plot(t, noise, label='Noise')
# plt.legend()
#
# plt.subplot(4, 1, 4)
# plt.plot(t, serie_timp, label='Seria de timp', color='red')
#
#
# plt.legend()
# plt.tight_layout()
#
#
#
# def mediere_exponentiala(serie, alpha):
#     result = np.zeros_like(serie, dtype=float)
#     result[0] = serie[0]  # Initializam cu prima valoare din seria originala
#
#
#     for t in range(1, len(serie)):
#         result[t] = alpha * serie[t] + (1 - alpha) * result[t-1]
#
#     return result
#
# def calculeaza_eroare(serie_originala, serie_noua):
#     return np.mean((serie_originala - serie_noua)**2)

# # dam parametrii
# alpha_initial = 0.5
# alpha_testate = np.linspace(0, 1, 100)  # alegem 100 valori de la 1 la 100
# serie_originala = serie_timp  # alocam seria generata mai sus
#
# # incercam sa gasim un alpha bun prin try & error
# eroare_minima = float('inf')
# alpha_optim = None
#
# for alpha in alpha_testate:
#     serie_noua = mediere_exponentiala(serie_originala, alpha)
#     eroare = calculeaza_eroare(serie_originala, serie_noua)
#
#     if eroare < eroare_minima:
#         eroare_minima = eroare
#         alpha_optim = alpha
#
#
# print(f'Alpha optim: {alpha_optim}')
# serie_noua_optim = mediere_exponentiala(serie_originala, alpha_optim)
#
# # Seria originala si cea rezultata
# plt.figure(figsize=(12, 6))
# plt.plot(t, serie_originala, label='Seria Originala', color='blue')
# plt.plot(t, serie_noua_optim, label=f'Seria Noua (α={alpha_optim:.3f})', color='red', linestyle='dashed')
# plt.title('Mediere Exponentiala si Alpha Optim')
# plt.xlabel('Timp')
# plt.ylabel('Valoare')
# plt.legend()
# plt.show()
#
#





import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

N = 1000
t = np.arange(N)
trend_exp = np.exp(0.005 * t)  # generat trend exponential

f1, f2 = 0.1, 0.01
season = 5 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t)
noise = np.random.normal(0, 1, N)
serie_timp_neuniforma = trend_exp + season + noise


# afisare trend exp
plt.figure(figsize=(12, 6))
plt.subplot(4, 1, 1)
plt.plot(t, trend_exp, label='Trend Exponential')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, season, label='Season')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, noise, label='Noise')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, serie_timp_neuniforma, label='Seria de timp neuniforma', color='red')
plt.legend()

plt.tight_layout()

# medierea exp
def mediere_exponentiala(serie, alpha):
    result = np.zeros_like(serie, dtype=float)
    result[0] = serie[0]  # initializam cu prima valore din seria originala

    for t in range(1, len(serie)):
        result[t] = alpha * serie[t] + (1 - alpha) * result[t-1]

    return result

def calculeaza_eroare(serie_originala, serie_noua):
    return np.mean((serie_originala - serie_noua)**2)

# dam parametrii
alpha_initial = 0.5
alpha_testate = np.linspace(0, 1, 100)
serie_originala = serie_timp_neuniforma


# # incercam sa gasim un alpha bun prin try & error

eroare_minima = float('inf')
alpha_optim = None

for alpha in alpha_testate:
    serie_noua = mediere_exponentiala(serie_originala, alpha)
    eroare = calculeaza_eroare(serie_originala, serie_noua)

    if eroare < eroare_minima:
        eroare_minima = eroare
        alpha_optim = alpha


print(f'Alpha optim: {alpha_optim}')
serie_noua_optim = mediere_exponentiala(serie_originala, alpha_optim)

# # Seria originala si cea rezultata
plt.figure(figsize=(12, 6))
plt.plot(t, serie_originala, label='Seria Originala', color='blue')
plt.plot(t, serie_noua_optim, label=f'Seria Noua (α={alpha_optim:.3f})', color='red', linestyle='dashed')
plt.title('Mediere Exponentiala si Alpha Optim')
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.legend()





# Parametrii seriei de timp anterioare
t = np.arange(N)
serie_timp = trend_exp + season + noise

# orizontul modelului MA , q
q = 3

# Generam termenii de eroare conform unei distributii normale standard
eroare = np.random.normal(0, 1, N)

# calcul coef modelului MA
model_ma = sm.tsa.arima.model.ARIMA(serie_timp, order=(0, 0, q), exog=eroare)
fit_model_ma = model_ma.fit()


# Generarea seriei temporale cu modelul MA aplicat
serie_ma = fit_model_ma.fittedvalues + trend_exp + season

plt.figure(figsize=(12, 6))
plt.plot(t, serie_timp, label='Seria de timp originala', color='blue')
plt.plot(t, serie_ma, label=f'Seria generata cu MA({q})', color='red', linestyle='dashed')
plt.title(f'Model MA({q}) si Seria Generata')
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.legend()
plt.show()
