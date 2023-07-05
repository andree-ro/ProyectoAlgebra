# import aritmethic, compound_numbers, equations, matrix
#
# print(aritmethic.parse_aritmethic("1+2"))
# string = "(3+2i)-(4-5i)+(2+7i)"
# print(compound_numbers.compound_parse(string))

def validar_dimensiones(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])

    if filas1 == filas2 and columnas1 == columnas2:
        return True
    else:
        return False

def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado

def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            resta = matriz1[i][j] - matriz2[i][j]
            fila.append(resta)
        resultado.append(fila)

    return resultado

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

# Función para mostrar una matriz en forma legible
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para mostrar el procedimiento paso a paso
def mostrar_procedimiento(matriz1, matriz2, resultado, operacion):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    filas_r = len(resultado)
    columnas_r = len(resultado[0])

    print("\nProcedimiento:")
    print(f"Operación: {operacion}\n")

    print("Matriz 1:")
    mostrar_matriz(matriz1)

    print("\nMatriz 2:")
    mostrar_matriz(matriz2)

    print("\nResultado:")
    mostrar_matriz(resultado)

    print("\nPasos:")

    if operacion == "Suma" or operacion == "Resta":
        for i in range(filas1):
            for j in range(columnas1):
                print(f"\n{matriz1[i][j]} {operacion} {matriz2[i][j]} = {resultado[i][j]}")
    elif operacion == "Multiplicación":
        for i in range(filas1):
            for j in range(columnas2):
                paso = []
                for k in range(columnas1):
                    paso.append(f"{matriz1[i][k]} * {matriz2[k][j]}")
                paso_str = " + ".join(paso)
                print(f"\n{paso_str} = {resultado[i][j]}")