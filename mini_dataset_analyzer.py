"""
Módulo que contiene el programa mini_dataset_analyzer.
Permite analizar un conjunto de datos ingresados por el usuario.
"""


def mini_dataset_analyzer():
    """
    Esta función permite ingresar un conjunto de datos numéricos
    y calcula el promedio, valor máximo, valor mínimo y
    la cantidad de registros.
    """

    datos = []

    cantidad = int(input("¿Cuántos datos desea ingresar?: "))

    for i in range(cantidad):
        numero = float(input(f"Ingrese el dato #{i + 1}: "))
        datos.append(numero)

    if len(datos) > 0:
        suma = 0

        for valor in datos:
            suma += valor

        promedio = suma / len(datos)
        maximo = max(datos)
        minimo = min(datos)
        cantidad_registros = len(datos)
    else:
        promedio = 0
        maximo = 0
        minimo = 0
        cantidad_registros = 0

    print("\n--- RESULTADOS DEL DATASET ---")
    print("Promedio:", promedio)
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)
    print("Cantidad de registros:", cantidad_registros)


mini_dataset_analyzer()
