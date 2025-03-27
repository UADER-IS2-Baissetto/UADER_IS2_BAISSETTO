import matplotlib.pyplot as plt

# Función para calcular la secuencia de Collatz y contar las iteraciones
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
        iterations += 1
    return iterations

# Lista para almacenar los resultados (número de inicio y número de iteraciones)
numbers = []
iterations = []

# Calcular las iteraciones para los números entre 1 y 10000
for n in range(1, 10001):
    iter_count = collatz_iterations(n)
    numbers.append(n)
    iterations.append(iter_count)

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(iterations, numbers, alpha=0.5, color='b', s=1)  # Ajuste de tamaño y color de los puntos
plt.title("Número de Iteraciones para la Conjetura de Collatz", fontsize=14)
plt.xlabel("Número de Iteraciones", fontsize=12)
plt.ylabel("Número de Inicio (n)", fontsize=12)
plt.grid(True)
plt.show()