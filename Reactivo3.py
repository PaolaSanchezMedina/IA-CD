#Sánchez Medina Paola Guadalupe

import numpy as np
import matplotlib.pyplot as plt

#Ejes
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
yfacecream = np.array([2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900])
yfacewash = np.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])
ytoothpaste = np.array([5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400])
ybathingsoap = np.array([9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400])
yshampoo = np.array([1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800])
ymoisturizer = np.array([1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760])

#Crear las gráficas
plt.plot(x, yfacecream, label="facecream", marker = 'o')
plt.plot(x, yfacewash, label="facewash", marker = 'o')
plt.plot(x, ytoothpaste, label="toothpaste", marker = 'o')
plt.plot(x, ybathingsoap, label="bathingsoap", marker = 'o')
plt.plot(x, yshampoo, label="shampoo", marker = 'o')
plt.plot(x, ymoisturizer, label="moisturizer", marker = 'o')

#Etiquetas de los ejes
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')

#Título la gráfica
plt.title('Gráfica del reactivo 3')

#Etiquetas
plt.legend()

#Mostrar la gráfica
plt.show()