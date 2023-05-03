"""
    Tirar un dado de 6 caras (10,000 veces)
    Calcular media y desviación estándar
    Gráficar histograma

"""

import random
import numpy as np
import matplotlib.pyplot as plt

tiradas = np.empty(10000, dtype=int)

def tirarDado():
    dado = random.randint(1,6)
    dado2 = random.randint(1,6)
    return (dado + dado2)

#Llena el arreglo con 10,000 tiradas
print("Se llena el arreglo con 10,000 tiradas")
x = 0
for x in range(len(tiradas)):
    tirada = tirarDado()
    tiradas[x] = tirada
    x += 1
hello = 6*5
print(hello)

#Calcula la media y la desviación estándar
# print("La media es: ", np.mean(tiradas))
# print("La desviación estándar es: ", np.std(tiradas))

# plt.hist(tiradas)
# plt.show()