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

# Menú principal
while True:
    print("Operaciones con Matrices:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1" or opcion == "2" or opcion == "3":
        filas1 = int(input("Ingrese el número de filas de la matriz 1: "))
        columnas1 = int(input("Ingrese el número de columnas de la matriz 1: "))
        filas2 = int(input("Ingrese el número de filas de la matriz 2: "))
        columnas2 = int(input("Ingrese el número de columnas de la matriz 2: "))

        print("\nIngrese los elementos de la matriz 1:")
        matriz1 = []
        for i in range(filas1):
            fila = []
            for j in range(columnas1):
                elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
                fila.append(elemento)
            matriz1.append(fila)

        print("\nIngrese los elementos de la matriz 2:")
        matriz2 = []
        for i in range(filas2):
            fila = []
            for j in range(columnas2):
                elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
                fila.append(elemento)
            matriz2.append(fila)

        if opcion == "1":
            if validar_dimensiones(matriz1, matriz2):
                resultado = sumar_matrices(matriz1, matriz2)
                mostrar_procedimiento(matriz1, matriz2, resultado, "Suma")
                print("\nLa suma de las matrices es:")
                mostrar_matriz(resultado)
            else:
                print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
        elif opcion == "2":
            if validar_dimensiones(matriz1, matriz2):
                resultado = restar_matrices(matriz1, matriz2)
                mostrar_procedimiento(matriz1, matriz2, resultado, "Resta")
                print("\nLa resta de las matrices es:")
                mostrar_matriz(resultado)
            else:
                print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
        elif opcion == "3":
            if columnas1 == filas2:
                resultado = multiplicar_matrices(matriz1, matriz2)
                mostrar_procedimiento(matriz1, matriz2, resultado, "Multiplicación")
                print("\nEl producto de las matrices es:")
                mostrar_matriz(resultado)
            else:
                print("El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2. La operación no es válida.")
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")
