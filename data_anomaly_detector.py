#data_anomaly_detector

def data_anomaly_detector(): 
    
    temperatures = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar temperatura")
        print("2. Ver temperaturas")
        print("3. Detectar anomalías")
        print("4. Ver estadísticas")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                temp = float(input("Ingrese la temperatura: "))
                temperatures.append(temp)
                print("Temperatura registrada exitosamente.")

            case "2":
                print("\nTemperaturas registradas:")
                if not temperatures:
                    print("No hay temperaturas registradas.")
                else:
                    for t in temperatures:
                        print(t)

            case "3":
                print("\nAnomalías detectadas:")
                found_anomaly = False
                for t in temperatures:
                    if t > 50 or t < -10:
                        print(f"Anomalía detectada: {t}")
                        found_anomaly = True
            
                if not found_anomaly:
                    print("No se detectaron anomalías.")

            case "4":
                if not temperatures:
                    print("No hay datos para mostrar estadísticas.")
                else:
                    average = sum(temperatures) / len(temperatures)
                    maximum = max(temperatures)
                    minimum = min(temperatures)

                    print("\n--- ESTADÍSTICAS ---")
                    print(f"Promedio: {average:.2f}")
                    print(f"Máximo: {maximum}")
                    print(f"Mínimo: {minimum}")
                    print(f"Cantidad de datos: {len(temperatures)}")

            case "5":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

data_anomaly_detector()