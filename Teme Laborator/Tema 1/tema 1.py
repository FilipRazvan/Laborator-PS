import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage, fft
from scipy.fft import dctn, idctn
from skimage.color import rgb2ycbcr, ycbcr2rgb
from sklearn.metrics import mean_squared_error

# ////////////////////////////////////////////////////////////////////////////////
# X = misc.ascent()
# plt.imshow(X, cmap=plt.cm.gray)
# plt.show()
#
# Y1 = dctn(X, type=1)
# Y2 = dctn(X, type=2)
# Y3 = dctn(X, type=3)
# Y4 = dctn(X, type=4)
# freq_db_1 = 20*np.log10(abs(Y1))
# freq_db_2 = 20*np.log10(abs(Y2))
# freq_db_3 = 20*np.log10(abs(Y3))
# freq_db_4 = 20*np.log10(abs(Y4))
#
# plt.subplot(221).imshow(freq_db_1)
# plt.subplot(222).imshow(freq_db_2)
# plt.subplot(223).imshow(freq_db_3)
# plt.subplot(224).imshow(freq_db_4)
# plt.show()
#
#
# k = 120
#
# Y_ziped = Y2.copy()
# Y_ziped[k:] = 0
# X_ziped = idctn(Y_ziped)
#
# plt.imshow(X_ziped, cmap=plt.cm.gray)
# plt.show()
#
#
# Q_down = 10
#
# X_jpeg = X.copy()
# X_jpeg = Q_down*np.round(X_jpeg/Q_down);
#
# plt.subplot(121).imshow(X, cmap=plt.cm.gray)
# plt.title('Original')
# plt.subplot(122).imshow(X_jpeg, cmap=plt.cm.gray)
# plt.title('Down-sampled')
# plt.show()
#
#
#
# Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
#           [12, 12, 14, 19, 26, 28, 60, 55],
#           [14, 13, 16, 24, 40, 57, 69, 56],
#           [14, 17, 22, 29, 51, 87, 80, 62],
#           [18, 22, 37, 56, 68, 109, 103, 77],
#           [24, 35, 55, 64, 81, 104, 113, 92],
#           [49, 64, 78, 87, 103, 121, 120, 101],
#           [72, 92, 95, 98, 112, 100, 103, 99]]
#
# # Encoding
# x = X[:8, :8]
# y = dctn(x)
# y_jpeg = Q_jpeg*np.round(y/Q_jpeg)
#
# # Decoding
# x_jpeg = idctn(y_jpeg)
#
# # Results
# y_nnz = np.count_nonzero(y)
# y_jpeg_nnz = np.count_nonzero(y_jpeg)
#
# plt.subplot(121).imshow(x, cmap=plt.cm.gray)
# plt.title('Original')
# plt.subplot(122).imshow(x_jpeg, cmap=plt.cm.gray)
# plt.title('JPEG')
# plt.show()
#
# print('Componente în frecvență:' + str(y_nnz) +
#       '\nComponente în frecvență după cuantizare: ' + str(y_jpeg_nnz))
# //////////////////////////////////////////////////////////////////////////////////////////




# ////////// EX 1


# imaginea
X = misc.ascent()

# Matricea de cuantizare JPEG
Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

# Dimensiunile imaginii
height, width = X.shape

# Dimensiunile blocului 8x8
block_size = 8

# aplicam transformata DCT pe imaginea intreaga
Y = dctn(X, type=2)

# initializam o matrice pentru imaginea JPEG
Y_jpeg = np.zeros((height, width))

# cuantizeaza valorile obținute prin transformata DCT pentru fiecare bloc
for i in range(0, height, block_size):
    for j in range(0, width, block_size):
        # Selectează un bloc 8x8
        block = Y[i:i + block_size, j:j + block_size]

        # cuantizeaza blocul cu floor, dar menținem valorile întregi
        Y_jpeg[i:i + block_size, j:j + block_size] = np.floor(block / Q_jpeg)

# decodificam imaginea folosind transformata IDCT
X_jpeg = idctn(Y_jpeg, type=2)

# afisam img originala si cea jpeg
plt.subplot(121).imshow(X, cmap=plt.cm.gray)
plt.title('Original')
plt.subplot(122).imshow(X_jpeg, cmap=plt.cm.gray)
plt.title('JPEG')
plt.show()

# calculam componentele in frecventa nenule
y_nnz = np.count_nonzero(Y)
y_jpeg_nnz = np.count_nonzero(Y_jpeg)

print('Componente în frecventa pentru imaginea originala:', y_nnz)
print('Componente în frecventa pentru imaginea JPEG:', y_jpeg_nnz)






# ////////////////// EX 2

# # Imaginea
# X_color = misc.face()
#
# # Matricea de cuantizare JPEG
# Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
#                    [12, 12, 14, 19, 26, 28, 60, 55],
#                    [14, 13, 16, 24, 40, 57, 69, 56],
#                    [14, 17, 22, 29, 51, 87, 80, 62],
#                    [18, 22, 37, 56, 68, 109, 103, 77],
#                    [24, 35, 55, 64, 81, 104, 113, 92],
#                    [49, 64, 78, 87, 103, 121, 120, 101],
#                    [72, 92, 95, 98, 112, 100, 103, 99]])
#
# # Convertirea din RGB în Y'CbCr
# YCbCr = rgb2ycbcr(X_color)
#
# # Dimensiunile imaginii
# height, width, _ = X_color.shape
#
# # Dimensiunile blocului (8x8)
# block_size = 8
#
# # Aplică transformata DCT pe fiecare canal de culoare separat
# YCbCr_dct = YCbCr.copy()
#
# # Cuantizează valorile obținute prin transformata DCT pentru fiecare canal și bloc
# for i in range(0, height, block_size):
#     for j in range(0, width, block_size):
#         for k in range(3):
#             # Selectează un bloc 8x8 pentru fiecare canal de culoare
#             block = YCbCr_dct[i:i + block_size, j:j + block_size, k]
#
#             # Aplică transformata DCT
#             block_dct = dctn(block, type=2)  # Specify type=2 for DCT-II
#
#             # Cuantizează blocul
#             block_quantized = np.round(block_dct / Q_jpeg)
#
#             # Aduce blocul înapoi la scala inițială prin multiplicare cu matricea de cuantizare
#             block_quantized *= Q_jpeg
#
#             # Aplică transformata IDCT pentru decodificare
#             block_decoded = idctn(block_quantized, type=2)  # Specify type=2 for DCT-II
#
#             # Încorporează blocul decodificat în imaginea JPEG finală
#             YCbCr_dct[i:i + block_size, j:j + block_size, k] = block_decoded
#
# # Decodifică imaginea folosind transformata IDCT
# X_color_jpeg_dct = YCbCr_dct.copy()
#
# # Afișează imaginile originală și JPEG
# plt.figure(figsize=(12, 6))
#
# plt.subplot(121).imshow(X_color)
# plt.title('Original')
#
# plt.subplot(122).imshow(X_color_jpeg_dct.astype(np.uint8))
# plt.title('JPEG')
#
# plt.tight_layout()
# plt.show()
#
# # Calculează numărul de componente nenule în frecvență pentru imaginea originală (canalul Y)
# y_nnz_original = np.count_nonzero(dctn(YCbCr[:, :, 0], norm='ortho'))
#
# # Calculează numărul de componente nenule în frecvență pentru imaginea JPEG (canalul Y al imaginii decodificate)
# y_jpeg_nnz = np.count_nonzero(dctn(YCbCr_dct[:, :, 0], norm='ortho'))
#
# print('Componente în frecvență pentru imaginea originală (canalul Y):', y_nnz_original)
# print('Componente în frecvență pentru imaginea JPEG (canalul Y):', y_jpeg_nnz)








# #/////////////// EX 3
#
# # Funcție pentru calculul MSE intre doua imagini
# def calculate_mse(original, compressed):
#     return np.mean((original - compressed) ** 2)
#
# # Imaginea
# X = misc.ascent()
#
# # Matricea de cuantizare JPEG
# Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
#                    [12, 12, 14, 19, 26, 28, 60, 55],
#                    [14, 13, 16, 24, 40, 57, 69, 56],
#                    [14, 17, 22, 29, 51, 87, 80, 62],
#                    [18, 22, 37, 56, 68, 109, 103, 77],
#                    [24, 35, 55, 64, 81, 104, 113, 92],
#                    [49, 64, 78, 87, 103, 121, 120, 101],
#                    [72, 92, 95, 98, 112, 100, 103, 99]])
#
# # Dimensiunile imaginii
# height, width = X.shape
#
# # Dimensiunile blocului 8x8
# block_size = 8
#
# # Pragul MSE
# user_mse_threshold = 10000
#
# # aplicam transformata DCT pe toata imaginea
# Y = dctn(X, type=2)
#
# # initializam o matrice pentru imaginea JPEG
# Y_jpeg = np.zeros((height, width))
#
# # cuantizam valorile obținute prin transformata DCT pentru fiecare bloc 8x8
# for i in range(0, height, block_size):
#     for j in range(0, width, block_size):
#         # selectam bloc 8x8
#         block = Y[i:i + block_size, j:j + block_size]
#
#         # cuantizam blocul cu floor, dar menținem valorile întregi
#         Y_jpeg[i:i + block_size, j:j + block_size] = np.floor(block / Q_jpeg)
#
#         # Decodificam imaginea temporar pentru calculul MSE
#         X_temp = idctn(Y_jpeg, type=2)
#
#         # Calculam MSE intre imaginea originala si cea temporara
#         mse = calculate_mse(X, X_temp)
#
#         # Verificam daca MSE atinge sau scade sub pragul selectat
#         if mse <= user_mse_threshold:
#             break
#
# # decodificam imaginea folosind transformata IDCT
# X_jpeg = idctn(Y_jpeg, type=2)
#
# # afisam img originala si cea jpeg
# plt.subplot(121).imshow(X, cmap=plt.cm.gray)
# plt.title('Original')
# plt.subplot(122).imshow(X_jpeg, cmap=plt.cm.gray)
# plt.title('JPEG')
# plt.show()
#
# # calculam componentele in frecventa nenula
# y_nnz = np.count_nonzero(Y)
# y_jpeg_nnz = np.count_nonzero(Y_jpeg)
#
# print('Componente în frecventa pentru imaginea originala:', y_nnz)
# print('Componente în frecventa pentru imaginea JPEG:', y_jpeg_nnz)
# print('MSE între imaginea originala și cea JPEG:', calculate_mse(X, X_jpeg))