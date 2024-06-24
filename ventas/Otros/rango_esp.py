from datetime import datetime

print("--Ventas por rango de fecha--")
total = 0
fecha = input("Ingrese la primera fecha (YYYY-MM-DD): ")
fecha2 = input("Ingrese la segunda fecha (YYYY-MM-DD): ")

try:
    fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
    fecha2_dt = datetime.strptime(fecha2, "%Y-%m-%d")
except ValueError:
    print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
    exit()

for venta in ventas:
    venta_fecha = datetime.strptime(venta[1], "%Y-%m-%d")
    if fecha_dt <= venta_fecha <= fecha2_dt:
        total += venta[3] * venta[4]
        print(venta[0], venta[1], venta[2], venta[3], venta[4])

if total != 0:
    print(f"\nEl total de las ventas es: ${total}")
else:
    print("No se registran ventas para el rango de fechas.")