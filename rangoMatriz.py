import numpy as np

# Función para ingresar una matriz desde la consola
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

# Función para realizar la eliminación Gaussiana y calcular el rango
def calcular_rango(matriz):
    matriz_np = np.array(matriz)

    # Realizar la eliminación Gaussiana
    filas, columnas = matriz_np.shape
    rango = 0
    for i in range(min(filas, columnas)):
        print(f"\nEtapa {i+1}:")
        print(f"   Matriz actual:")
        for fila in matriz_np:
            print(f"   {fila}")
        print()

        if matriz_np[i, i] == 0:
            print(f"   No se puede hacer un pivote en la fila {i+1}.")
            continue

        print(f"   Pivote en la fila {i+1}: {matriz_np[i, i]}")

        rango += 1
        for j in range(i + 1, filas):
            coeficiente = matriz_np[j, i] / matriz_np[i, i]
            print(f"   Fila {j+1} -= ({coeficiente}) * Fila {i+1}")
            matriz_np[j, i:] -= coeficiente * matriz_np[i, i:]

    return rango

# Función para mostrar el paso a paso del cálculo del rango
def mostrar_paso_a_paso(matriz):
    print("\nProcedimiento para calcular el rango de la matriz:")
    print("1. La matriz original es:")
    for fila in matriz:
        print(f"   {fila}")

    rango = calcular_rango(matriz)

    print("\n2. Paso a paso del cálculo:")
    print(f"   El rango final de la matriz es: {rango}")
