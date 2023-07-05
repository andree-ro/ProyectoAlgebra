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


# Menú principal
while True:
    print("Cálculo de la Matriz Inversa:")
    print("1. Ingresar una matriz")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        filas = int(input("Ingrese el número de filas de la matriz: "))
        columnas = int(input("Ingrese el número de columnas de la matriz: "))

        matriz = ingresar_matriz(filas, columnas)
        matriz_inversa = calcular_inversa(matriz)

        if matriz_inversa is not None:
            print("\nProcedimiento paso a paso:")
            print("Matriz original:")
            mostrar_matriz(matriz)
            print("\nMatriz identidad extendida:")
            mostrar_matriz(np.concatenate((np.array(matriz), np.eye(filas)), axis=1))
            print("\nEliminación Gaussiana:")
            mostrar_matriz(np.array(matriz_inversa))
            print("\nLa matriz inversa es:")
            mostrar_matriz(matriz_inversa)
        else:
            print("\nLa matriz no tiene inversa.")
    elif opcion == "2":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")
