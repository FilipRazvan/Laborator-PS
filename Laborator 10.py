import numpy as np
import matplotlib.pyplot as plt
# # ex 1. part 1
#
# # declaram media si varianta
# media = 2
# varianta = 1.5
#
# # esantionam distributia gaussiana unidimensionala
# esantioane_unidimensionale = np.random.normal(media, np.sqrt(varianta), 1000)
#
# # afisam histrograma
# plt.hist(esantioane_unidimensionale, bins=50, density=True, alpha=0.6, color='g')
# plt.title('Distributie gaussiana unidimensionala')
# plt.xlabel('Valoare')
# plt.ylabel('Frecventa')
# plt.show()



# # ex 2 part 2 bidimensionala
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # declaram distributia gaussiana bidimensionala
#
# # Alta matrice covarianta random
# # medieBidimensionala = np.array([1, 2])
# # covariantaBidimensionala = np.array([[2, 1], [1, 2]])
#
#
# # Matrice covarianta wiki
# medieBidimensionala = np.array([0, 0])
# covariantaBidimensionala = np.array([[0.5,1], [1, 0.5]])
#
#
#
# # esantionare din distributia gauss bidim.
# esantioaneBidimensionale = np.random.multivariate_normal(medieBidimensionala, covariantaBidimensionala, 1000)
#
# # Afișare scatter plot
# plt.scatter(esantioaneBidimensionale[:, 0], esantioaneBidimensionale[:, 1], alpha=0.6, color='b')
# plt.title('Distributie gaussiana Bidimensionala')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()





import numpy as np
import matplotlib.pyplot as plt


d = 5  # setam dimensiunea spatiului de lucru
interval_lucru = [-1, 1]

# matricea de covarianta
def calcul_matrice_covarianta(d, interval_lucru):
    x = np.linspace(interval_lucru[0], interval_lucru[1], d)
    cij = np.outer(x, x)  # covarianta liniara x^Ty
    return cij

# esantionare din distrub gaussiana
def esantionare_proces_Gaussian(covarianța, num_esantioane=1):
    # esantionare din distrub normala multidimensionala
    esantioane = np.random.multivariate_normal(np.zeros(d), covarianța, num_esantioane)
    return esantioane



covarianta = calcul_matrice_covarianta(d, interval_lucru)
esantioane = esantionare_proces_Gaussian(covarianta, num_esantioane=6)

# afisam graficul
for i in range(esantioane.shape[0]):
    plt.plot(np.linspace(interval_lucru[0], interval_lucru[1], d), esantioane[i, :], label=f'Esantion {i+1}')

plt.title('Exemplu de eșantionare prin process Gaussian')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

