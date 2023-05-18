import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones
def f1(x):
    return x

def f2(x):
    return x ** 2

def f3(x):
    return x ** 3

# Crear los puntos x en el intervalo de 0 a 5 segundos con intervalos de 200 milisegundos
x = np.arange(0, 5, 0.2)

# Calcular los valores de y para cada función
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

# Crear la gráfica
plt.plot(x, y1, label='f(x) = x', linestyle='dashed', color='hotpink')
plt.plot(x, y2, label='f(x) = x^2', linestyle='dotted', color='purple')
plt.plot(x, y3, label='f(x) = x^3', linestyle='dashdot', color='lightblue')

#Etiquetas de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Valores de las funciones')

#Título la gráfica
plt.title('Gráfica de las funciones')

#Etiquetas
plt.legend()

#Mostrar la gráfica
plt.show()