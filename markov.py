import numpy as np


def ingresar_matriz():
    print("Ingrese la matriz de transición:")
    n = int(input("Ingrese el número de filas: "))
    m = int(input("Ingrese el número de columnas: "))

    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = float(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz

def multiplicar_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    resultado = []

    for i in range(filas1):
        fila = []
        for j in range(columnas2):
            suma = 0
            for k in range(columnas1):
                producto = matriz1[i][k] * matriz2[k][j]
                suma += producto
            fila.append(suma)
        resultado.append(fila)

    return resultado

def calcular_distribucion_estacionaria(matriz, estado_inicial, num_iteraciones):
    matriz_np = np.array(matriz)
    n = matriz_np.shape[0]

    distribucion_actual = np.array(estado_inicial, ndmin=2).T

    print("\nCalculando la distribución estacionaria:")

    for i in range(num_iteraciones):
        print(f"\nIteración {i + 1}:")
        print(f"Distribución actual:\n{distribucion_actual}")

        distribucion_nueva = multiplicar_matrices(matriz, distribucion_actual)
        distribucion_actual = distribucion_nueva

    distribucion_estacionaria = distribucion_actual

    return distribucion_estacionaria
