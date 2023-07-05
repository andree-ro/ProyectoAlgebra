import markov, matrizDeterminante, matrizInversa, opMatrices, rangoMatriz, sarrus
import numpy as np

while True:
    print('MENU')
    print('1. Operaciones entre matrices.')
    print('2. Matriz Inversa.')
    print('3. Rango de una Matriz.')
    print('4. Determinante de una matriz.')
    print('5. Siste de ecuaciones 3x3 por Sarrus.')
    print('6. Cadena de Markov.')
    print('7. Salir.')

    opcion = int(input('Ingrese la opcion deseada: '))

    if opcion == 1:
        print('-OPERADORES ENTRE MATRICES-')
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
                        elemento = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
                        fila.append(elemento)
                    matriz1.append(fila)

                print("\nIngrese los elementos de la matriz 2:")
                matriz2 = []
                for i in range(filas2):
                    fila = []
                    for j in range(columnas2):
                        elemento = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
                        fila.append(elemento)
                    matriz2.append(fila)

                if opcion == "1":
                    if opMatrices.validar_dimensiones(matriz1, matriz2):
                        resultado = opMatrices.sumar_matrices(matriz1, matriz2)
                        opMatrices.mostrar_procedimiento(matriz1, matriz2, resultado, "Suma")
                        print("\nLa suma de las matrices es:")
                        opMatrices.mostrar_matriz(resultado)
                    else:
                        print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
                elif opcion == "2":
                    if opMatrices.validar_dimensiones(matriz1, matriz2):
                        resultado = opMatrices.restar_matrices(matriz1, matriz2)
                        opMatrices.mostrar_procedimiento(matriz1, matriz2, resultado, "Resta")
                        print("\nLa resta de las matrices es:")
                        opMatrices.mostrar_matriz(resultado)
                    else:
                        print("Las matrices no tienen las mismas dimensiones. La operación no es válida.")
                elif opcion == "3":
                    if columnas1 == filas2:
                        resultado = opMatrices.multiplicar_matrices(matriz1, matriz2)
                        opMatrices.mostrar_procedimiento(matriz1, matriz2, resultado, "Multiplicación")
                        print("\nEl producto de las matrices es:")
                        opMatrices.mostrar_matriz(resultado)
                    else:
                        print(
                            "El número de columnas de la matriz 1 debe ser igual al número de filas de la matriz 2. La operación no es válida.")
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 2:
        print("MATRIZ INVERSA")
        while True:
            print("Cálculo de la Matriz Inversa:")
            print("1. Ingresar una matriz")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                filas = int(input("Ingrese el número de filas de la matriz: "))
                columnas = int(input("Ingrese el número de columnas de la matriz: "))

                matriz = matrizInversa.ingresar_matriz(filas, columnas)
                matriz_inversa = matrizInversa.calcular_inversa(matriz)

                if matriz_inversa is not None:
                    print("\nProcedimiento paso a paso:")
                    print("Matriz original:")
                    matrizInversa.mostrar_matriz(matriz)
                    print("\nMatriz identidad extendida:")
                    matrizInversa.mostrar_matriz(np.concatenate((np.array(matriz), np.eye(filas)), axis=1))
                    print("\nEliminación Gaussiana:")
                    matrizInversa.mostrar_matriz(np.array(matriz_inversa))
                    print("\nLa matriz inversa es:")
                    matrizInversa.mostrar_matriz(matriz_inversa)
                else:
                    print("\nLa matriz no tiene inversa.")
            elif opcion == "2":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 3:
        print('RANGO DE UNA MATRIZ')
        while True:
            print("Cálculo del Rango de una Matriz:")
            print("1. Ingresar una matriz")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                filas = int(input("Ingrese el número de filas de la matriz: "))
                columnas = int(input("Ingrese el número de columnas de la matriz: "))

                matriz = rangoMatriz.ingresar_matriz(filas, columnas)

                print("\nLa matriz ingresada es:")
                for fila in matriz:
                    print(f"   {fila}")

                rangoMatriz.mostrar_paso_a_paso(matriz)
            elif opcion == "2":
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 4:
        print('DETERMINANTE DE UNA MATRIZ')
        while True:
            print("\nCálculo del Determinante de una Matriz:")
            print("1. Ingresar una matriz")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                matriz = matrizDeterminante.ingresar_matriz()

                print("\nLa matriz ingresada es:")
                for fila in matriz:
                    print(f"   {fila}")

                determinante, etapas = matrizDeterminante.calcular_determinante(matriz)
                matrizDeterminante.mostrar_resultado(determinante, etapas)

            elif opcion == "2":
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")

    elif opcion == 5:
        print('SISTEMA DE ECUACIONES LINEALES')
        while True:
            print("\nSistema de ecuaciones lienales por Sarrus.")
            print("1.Ingresar el sistema de ecuaciones")
            print("2. Salir")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                sistema = sarrus.ingresar_sistema()
                sarrus.mostrar_procedimiento(sistema)

            elif opcion == "2":
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 6:
        print("CADENA DE MARKOV")
        while True:
            print('1. Ingresar cadena de Markov')
            print('2. Salir')
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                matriz = markov.ingresar_matriz()

                print("\nMatriz de transición:")
                print(np.array(matriz))

                estado_inicial = input("Ingrese el estado inicial separado por comas: ")
                estado_inicial = [float(x.strip()) for x in estado_inicial.split(",")]
                print(estado_inicial)

                num_iteraciones = int(input("Ingrese el número de iteraciones: "))

                distribucion_estacionaria = markov.calcular_distribucion_estacionaria(matriz, estado_inicial, num_iteraciones)

                print("\nLa distribución estacionaria es:")
                for i, probabilidad in enumerate(distribucion_estacionaria):
                    print(f"P({i}) = {probabilidad}")

            elif opcion == "2":
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                continue

    elif opcion == 7:
        print('Programa Finalizado')
        break

    else:
        print("Opcion invalida.")
        continue
