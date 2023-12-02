from skimage.metrics import peak_signal_noise_ratio
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# imaginea data
X = misc.face(gray=True)

# adaugam zgomot la imaginea anterioara
X_noisy = X + np.random.normal(0, 10, X.shape)

# aplicam filtru low pass pentru reducerea zgomotului
X_filtered = ndimage.gaussian_filter(X_noisy, sigma=1)

# calculam snr inainte si dupa filtrare
snr_before = peak_signal_noise_ratio(X, X_noisy)
snr_after = peak_signal_noise_ratio(X, X_filtered)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(X, cmap=plt.cm.gray)
plt.title('Imaginea originala')

plt.subplot(1, 3, 2)
plt.imshow(X_noisy, cmap=plt.cm.gray)
plt.title(f'Imaginea Cu zgomot\nSNR: {snr_before:.2f}')

plt.subplot(1, 3, 3)
plt.imshow(X_filtered, cmap=plt.cm.gray)
plt.title(f'Imaginea filtrata\nSNR: {snr_after:.2f}')

plt.show()
