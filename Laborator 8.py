import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm



N = 1000
t = np.arange(N)
trend = 0.02 * t**2 + 0.5 * t + 10
f1, f2 = 0.1, 0.01
season = 5 * np.sin(2 * np.pi * f1 * t) + 3 * np.cos(2 * np.pi * f2 * t)
noise = np.random.normal(0, 1, N)
serie_timp = trend + season + noise

plt.figure(figsize=(12, 6))
plt.subplot(4, 1, 1)
plt.plot(t, trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, season, label='Season')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, noise, label='Noise')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, serie_timp, label='Seria de timp', color='red')
plt.legend()

plt.tight_layout()



# Calc vect de autocorelatie
autocorrelation = np.correlate(serie_timp, serie_timp, mode='full') / np.max(np.correlate(serie_timp, serie_timp, mode='full'))

# Afișarea vectorului de autocorelație
plt.figure(figsize=(10, 4))
plt.stem(autocorrelation)
plt.title('Vector de Autocorelatie')
plt.xlabel('Lag')
plt.ylabel('Autocorelatie')

plt.show()



# Se foloseste seria de timp generata anterior
# time_series = trend + season + noise

# ordinul modelului AR (de exemplu, p = 2)
p = 2

# calculam modelul AR
model = sm.tsa.AutoReg(serie_timp, lags=p)
ar_model = model.fit()

# Realizarea predicțiilor
predictions = ar_model.predict(start=p, end=len(serie_timp) - 1)

plt.figure(figsize=(12, 6))
plt.plot(t, serie_timp, label='Seria de timp originala', color='blue')
plt.plot(t[p:], predictions, label=f'Predictii AR({p})', color='red', linestyle='dashed')
plt.title(f'Model AR({p}) și Predictii')
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.legend()
plt.show()


