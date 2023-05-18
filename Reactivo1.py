#Sánchez Medina Paola Guadalupe

import numpy as np
import matplotlib.pyplot as plt

#Ejes
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700,412800, 300200])

#Crear la gráfica
plt.plot(x, y)

#Etiquetas de los ejes
plt.xlabel('Número de mes')
plt.ylabel('Beneficio total')

#Título la gráfica
plt.title('Gráfica del reactivo 1')

#Etiquetas
plt.legend()

#Mostrar la gráfica
plt.show()