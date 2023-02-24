import matplotlib.pyplot as plt
import numpy as np

meses = np.array(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
x = np.array([1, 6, 3, 2, 0, 0, 1, 0, 1, 1, 1, 5])

plt.bar(meses, x)
plt.show()