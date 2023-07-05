import numpy as np


# Función para ingresar una matriz desde la consola
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz


# Función para calcular la matriz inversa
def calcular_inversa(matriz):
    try:
        matriz_np = np.array(matriz)

        # Crear una matriz identidad del mismo tamaño
        matriz_identidad = np.eye(matriz_np.shape[0])

        # Concatenar la matriz original y la matriz identidad
        matriz_extendida = np.concatenate((matriz_np, matriz_identidad), axis=1)

        # Realizar eliminación Gaussiana
        for i in range(matriz_extendida.shape[0]):
            # Hacer el pivote igual a 1
            pivote = matriz_extendida[i][i]
            matriz_extendida[i] /= pivote

            # Restar la fila pivote de las demás filas
            for j in range(matriz_extendida.shape[0]):
                if j != i:
                    factor = matriz_extendida[j][i]
                    matriz_extendida[j] -= factor * matriz_extendida[i]

        # Extraer la matriz inversa de la parte derecha de la matriz extendida
        matriz_inversa = matriz_extendida[:, matriz_np.shape[1]:]
        return matriz_inversa.tolist()
    except np.linalg.LinAlgError:
        return None


# Función para mostrar una matriz en forma legible
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
