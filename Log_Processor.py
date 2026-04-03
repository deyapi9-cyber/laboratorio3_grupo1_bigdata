def procesar_logs(logs):
    conteo = {}

    for log in logs:
        partes = log.split(" ")
        tipo = partes[0]

        if tipo in conteo:
            conteo[tipo] += 1
        else:
            conteo[tipo] = 1

    return conteo


def mostrar_resultados(conteo):
    print("\n--- Resultados del análisis ---")
    for tipo, cantidad in conteo.items():
        print(f"{tipo}: {cantidad}")


def ingresar_logs():
    logs = []

    print("\nIngrese logs (escriba 'fin' para terminar):")

    while True:
        log = input("> ")

        if log.lower() == "fin":
            break

        logs.append(log)

    return logs


def leer_archivo(nombre_archivo):
    logs = []

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                logs.append(linea.strip())
    except:
        print("Error: no se pudo leer el archivo")

    return logs


def main():
    while True:
        print("\n=== PROCESADOR DE LOGS ===")
        print("1. Ingresar logs manualmente")
        print("2. Leer logs desde archivo")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            logs = ingresar_logs()
            resultado = procesar_logs(logs)
            mostrar_resultados(resultado)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del archivo: ")
            logs = leer_archivo(nombre)
            resultado = procesar_logs(logs)
            mostrar_resultados(resultado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


main()