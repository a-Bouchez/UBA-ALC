import numpy as np
import matplotlib.pyplot as plt  # Librería para graficar

# Crear la matriz y resolver el sistema para calcular a, b y c
A = np.array([
    [1**2, 1, 1],
    [2**2, 2, 1],
    [3**2, 3, 1]
])
b = np.array([1, 2, 0])

# Resolver el sistema Ax = b
a, b, c = np.linalg.solve(A, b)

# Datos de los puntos dados
xx = np.array([1, 2, 3])
yy = np.array([1, 2, 0])

# Generar 100 puntos equiespaciados entre 0 y 4
x = np.linspace(0, 4, 100)

# Definir la función cuadrática
f = lambda t: a * t**2 + b * t + c

# Graficar los puntos dados
plt.plot(xx, yy, 'r*', label="Puntos dados")

# Graficar la parábola
plt.plot(x, f(x), 'b-', label="Parábola ajustada")

# Mostrar la gráfica con leyenda
plt.legend()
plt.show()
