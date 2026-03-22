datos = []

cantidad = int(input("¿Cuántos datos desea ingresar?: "))

for i in range(cantidad):
    numero = float(input(f"Ingrese el dato #{i + 1}: "))
    datos.append(numero)

suma = 0

for valor in datos:
    suma += valor

promedio = suma / len(datos)
maximo = max(datos)
minimo = min(datos)
cantidad_registros = len(datos)

print("\n--- RESULTADOS DEL DATASET ---")
print("Promedio:", promedio)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Cantidad de registros:", cantidad_registros)
