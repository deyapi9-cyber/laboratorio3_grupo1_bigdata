# 1 Project mass_sales_analyzer

# Project mass_sales_analyzer

sales = []

sales_count = int(input("¿Cuántas ventas desea registrar?: "))

for i in range(sales_count):
    print("\nVenta", i + 1)
    
    product = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    quantity = int(input("Ingrese la cantidad vendida: "))

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": price * quantity
    }

    sales.append(sale)

total_sales = 0
largest_sale = sales[0]

for sale in sales:
    total_sales += sale["total"]

    if sale["total"] > largest_sale["total"]:
        largest_sale = sale

average_sales = total_sales / len(sales)

print("\n--- RESULTADOS ---")

option = "results"

match option:
    case "results":
        print("Total vendido:", total_sales)
        print("Promedio de ventas:", average_sales)
        print("Venta más grande:")
        print("Producto:", largest_sale["product"])
        print("Total:", largest_sale["total"])