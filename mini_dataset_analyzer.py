"""
Módulo que contiene el programa mini_dataset_analyzer.
Permite analizar un conjunto de datos ingresados por el
usuario.
"""


def mini_dataset_analyzer():
    """
    Esta función permite ingresar un conjunto de datos numéricos
    y calcula el promedio, valor máximo, valor mínimo y
    la cantidad de registros. En este caso los datos serán edades de
    colaboradores de una empresa.
    """

    data = []

    amount = int(input("¿Cuantas datos desea ingresar?: "))

    for i in range(amount):
        number = float(input(f"Ingrese el datos #{i + 1}: "))
        data.append(number)
    if len(data) > 0:
        addition = 0

        for value in data:
            addition += value

        average = addition / len(data)
        maximum = max(data)
        minimum = min(data)
        number_of_records = len(data)
    else:
        average = 0
        maximum = 0
        minimum = 0
        number_of_records = 0

    print("\n--- Resultados de DATASET ---")
    print("Promedio: ", average)
    print("Valor máximo: ", maximum)
    print("Valor mínimmo: ", minimum)
    print("Cantidad de registros ingresados: ", number_of_records)


mini_dataset_analyzer()
