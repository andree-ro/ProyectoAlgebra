# Función para ingresar un sistema de ecuaciones lineales
def ingresar_sistema():
    sistema = []
    print("Ingrese los coeficientes y las constantes del sistema de ecuaciones:")

    for i in range(3):
        ecuacion = []
        for j in range(4):
            elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            ecuacion.append(elemento)
        sistema.append(ecuacion)

    return sistema

# Función para calcular el determinante de una matriz 3x3
def calcular_determinante(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]
    d = matriz[1][0]
    e = matriz[1][1]
    f = matriz[1][2]
    g = matriz[2][0]
    h = matriz[2][1]
    i = matriz[2][2]

    determinante = a*e*i + b*f*g + c*d*h - c*e*g - a*f*h - b*d*i
    return determinante

# Función para resolver el sistema de ecuaciones utilizando el método de Sarrus
def resolver_sistema(sistema):
    coeficientes = [[sistema[0][0], sistema[0][1], sistema[0][2]],
                    [sistema[1][0], sistema[1][1], sistema[1][2]],
                    [sistema[2][0], sistema[2][1], sistema[2][2]]]

    constantes = [sistema[0][3], sistema[1][3], sistema[2][3]]

    determinante_principal = calcular_determinante(coeficientes)

    x_coeficientes = [[constantes[0], coeficientes[0][1], coeficientes[0][2]],
                      [constantes[1], coeficientes[1][1], coeficientes[1][2]],
                      [constantes[2], coeficientes[2][1], coeficientes[2][2]]]

    y_coeficientes = [[coeficientes[0][0], constantes[0], coeficientes[0][2]],
                      [coeficientes[1][0], constantes[1], coeficientes[1][2]],
                      [coeficientes[2][0], constantes[2], coeficientes[2][2]]]

    z_coeficientes = [[coeficientes[0][0], coeficientes[0][1], constantes[0]],
                      [coeficientes[1][0], coeficientes[1][1], constantes[1]],
                      [coeficientes[2][0], coeficientes[2][1], constantes[2]]]

    determinante_x = calcular_determinante(x_coeficientes)
    determinante_y = calcular_determinante(y_coeficientes)
    determinante_z = calcular_determinante(z_coeficientes)

    x = determinante_x / determinante_principal
    y = determinante_y / determinante_principal
    z = determinante_z / determinante_principal

    return x, y, z

# Función para mostrar el resultado del sistema de ecuaciones
def mostrar_resultado(x, y, z):
    print("\nEl sistema de ecuaciones tiene la siguiente solución:")
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")

# Función para mostrar el procedimiento paso a paso
def mostrar_procedimiento(sistema):
    print("\nProcedimiento paso a paso:")
    print("1. Ingrese los coeficientes y las constantes del sistema de ecuaciones.")

    for i in range(3):
        for j in range(4):
            print(f"   Ingrese el elemento [{i+1}][{j+1}]: {sistema[i][j]}")

    print("\n2. Calcule el determinante principal del sistema de ecuaciones.")

    print("   Determinante Principal = (a*e*i) + (b*f*g) + (c*d*h) - (c*e*g) - (a*f*h) - (b*d*i)")
    print(f"                         = ({sistema[0][0]} * {sistema[1][1]} * {sistema[2][2]}) + "
          f"({sistema[0][1]} * {sistema[1][2]} * {sistema[2][0]}) + ({sistema[0][2]} * {sistema[1][0]} * {sistema[2][1]}) - "
          f"({sistema[0][2]} * {sistema[1][1]} * {sistema[2][0]}) - ({sistema[0][0]} * {sistema[1][2]} * {sistema[2][1]}) - "
          f"({sistema[0][1]} * {sistema[1][0]} * {sistema[2][2]})")

    determinante_principal = calcular_determinante(sistema)

    print(f"                         = {determinante_principal}\n")

    x_coeficientes = [[sistema[0][3], sistema[0][1], sistema[0][2]],
                      [sistema[1][3], sistema[1][1], sistema[1][2]],
                      [sistema[2][3], sistema[2][1], sistema[2][2]]]

    y_coeficientes = [[sistema[0][0], sistema[0][3], sistema[0][2]],
                      [sistema[1][0], sistema[1][3], sistema[1][2]],
                      [sistema[2][0], sistema[2][3], sistema[2][2]]]

    z_coeficientes = [[sistema[0][0], sistema[0][1], sistema[0][3]],
                      [sistema[1][0], sistema[1][1], sistema[1][3]],
                      [sistema[2][0], sistema[2][1], sistema[2][3]]]

    determinante_x = calcular_determinante(x_coeficientes)
    determinante_y = calcular_determinante(y_coeficientes)
    determinante_z = calcular_determinante(z_coeficientes)

    print("3. Calcule los determinantes de las incógnitas x, y y z.")

    print("   Determinante X = (constante_x * coeficiente_y * coeficiente_z) + "
          "(coeficiente_x * constante_y * coeficiente_z) + "
          "(coeficiente_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(constante_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * constante_y * coeficiente_z)")

    print(f"                 = ({sistema[0][3]} * {sistema[0][1]} * {sistema[0][2]}) + "
          f"({sistema[1][3]} * {sistema[1][1]} * {sistema[1][2]}) + "
          f"({sistema[2][3]} * {sistema[2][1]} * {sistema[2][2]}) - "
          f"({sistema[2][3]} * {sistema[1][1]} * {sistema[0][2]}) - "
          f"({sistema[0][3]} * {sistema[1][1]} * {sistema[2][2]}) - "
          f"({sistema[1][3]} * {sistema[2][1]} * {sistema[0][2]})")

    print(f"                 = {determinante_x}\n")

    print("   Determinante Y = (coeficiente_x * constante_y * coeficiente_z) + "
          "(constante_x * coeficiente_y * coeficiente_z) + "
          "(coeficiente_x * coeficiente_y * constante_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * constante_y * constante_z) - "
          "(constante_x * coeficiente_y * coeficiente_z)")

    print(f"                 = ({sistema[0][0]} * {sistema[0][3]} * {sistema[0][2]}) + "
          f"({sistema[1][0]} * {sistema[1][3]} * {sistema[1][2]}) + "
          f"({sistema[2][0]} * {sistema[2][3]} * {sistema[2][2]}) - "
          f"({sistema[0][0]} * {sistema[1][3]} * {sistema[2][2]}) - "
          f"({sistema[0][3]} * {sistema[1][0]} * {sistema[2][2]}) - "
          f"({sistema[1][3]} * {sistema[2][0]} * {sistema[0][2]})")

    print(f"                 = {determinante_y}\n")

    print("   Determinante Z = (coeficiente_x * coeficiente_y * constante_z) + "
          "(coeficiente_x * constante_y * coeficiente_z) + "
          "(constante_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * coeficiente_y * coeficiente_z) - "
          "(coeficiente_x * constante_y * coeficiente_z) - "
          "(constante_x * coeficiente_y * constante_z)")

    print(f"                 = ({sistema[0][0]} * {sistema[0][1]} * {sistema[0][3]}) + "
          f"({sistema[1][0]} * {sistema[1][1]} * {sistema[1][3]}) + "
          f"({sistema[2][0]} * {sistema[2][1]} * {sistema[2][3]}) - "
          f"({sistema[0][0]} * {sistema[1][1]} * {sistema[2][3]}) - "
          f"({sistema[0][1]} * {sistema[1][3]} * {sistema[2][0]}) - "
          f"({sistema[0][3]} * {sistema[1][1]} * {sistema[2][0]})")

    print(f"                 = {determinante_z}\n")

    print("4. Calcule las soluciones del sistema de ecuaciones.")

    x = determinante_x / determinante_principal
    y = determinante_y / determinante_principal
    z = determinante_z / determinante_principal

    print(f"   x = Determinante X / Determinante Principal")
    print(f"     = {determinante_x} / {determinante_principal}")
    print(f"     = {x}\n")

    print(f"   y = Determinante Y / Determinante Principal")
    print(f"     = {determinante_y} / {determinante_principal}")
    print(f"     = {y}\n")

    print(f"   z = Determinante Z / Determinante Principal")
    print(f"     = {determinante_z} / {determinante_principal}")
    print(f"     = {z}\n")

    mostrar_resultado(x, y, z)

# Programa principal
print("Programa para resolver un sistema de ecuaciones lineales 3x3 por el método de Sarrus.\n")

sistema = ingresar_sistema()

mostrar_procedimiento(sistema)
