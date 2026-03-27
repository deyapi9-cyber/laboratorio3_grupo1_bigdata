# Data Anomaly Detector

temperatures = []

while True:
    print("\n--- MENÚ ---")
    print("1. Register temperature")
    print("2. View temperatures")
    print("3. Detect anomalies")
    print("4. View statistics")
    print("5. Exit")

    option = input("Select an option: ")

    match option:
        case "1":
            temp = float(input("Enter temperature: "))
            temperatures.append(temp)
            print("Temperature registered successfully.")

        case "2":
            print("\nRegistered Temperatures:")
            if not temperatures:
                print("No temperatures recorded.")
            else:
                for t in temperatures:
                    print(t)

        case "3":
            print("\nDetected Anomalies:")
            found_anomaly = False
            for t in temperatures:
                if t > 50 or t < -10:
                    print(f"Anomaly detected: {t}")
                    found_anomaly = True
            
            if not found_anomaly:
                print("No anomalies detected.")

        case "4":
            if not temperatures:
                print("No data to show statistics.")
            else:
                average = sum(temperatures) / len(temperatures)
                maximum = max(temperatures)
                minimum = min(temperatures)

                print("\n--- STATISTICS ---")
                print(f"Average: {average:.2f}")
                print(f"Maximum: {maximum}")
                print(f"Minimum: {minimum}")
                print(f"Data count: {len(temperatures)}")

        case "5":
            print("Exiting program...")
            break

        case _:
            print("Invalid option. Please try again.")