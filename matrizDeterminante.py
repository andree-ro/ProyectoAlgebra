import numpy as np


# Function to enter a matrix from the console
def ingresar_matriz():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matriz = []
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    return matriz


# Function to calculate the determinant of a matrix by the cofactor method
def calcular_determinante(matriz):
    matriz_np = np.array(matriz)
    n = matriz_np.shape[0]
    etapas = []

    def mostrar_etapa(matriz, etapa):
        print(f"\nEtapa {etapa + 1}:")
        print("Matriz actual:")
        for fila in matriz:
            print(f"   {fila}")

    mostrar_etapa(matriz_np, -1)

    def calcular_cofactor(matriz, fila, columna):
        submatriz = np.delete(np.delete(matriz, fila, axis=0), columna, axis=1)
        print(f"Submatriz:")
        print(submatriz)
        return (-1) ** (fila + columna) * np.linalg.det(submatriz)

    for i in range(n):
        etapa = {}
        etapa["Paso"] = f"Paso {i + 1}"

        cofactores = [calcular_cofactor(matriz_np, 0, j) for j in range(n)]
        etapa["Cofactores"] = cofactores

        determinante_parcial = matriz_np[0, i] * cofactores[i]
        etapa["Determinante parcial"] = determinante_parcial

        etapas.append(etapa)
        mostrar_etapa(matriz_np, i)

    determinante = np.sum([etapa["Determinante parcial"] for etapa in etapas])
    return determinante, etapas


# Function to show the result of the calculation of the determinant and the procedure step by step
def mostrar_resultado(determinante, etapas):
    print("\nProcedimiento paso a paso:")
    for etapa in etapas:
        print(etapa)
    print(f"\nEl determinante de la matriz es: {determinante}")
