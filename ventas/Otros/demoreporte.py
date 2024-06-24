fecha=input()
for venta in ventas:
    if venta[1] ==fecha:
        a=a+venta[2]
        print(venta[0]," ",venta[1]," ",venta[2])
    print(f"total, {a}")
    
#rangos de fecha

fecha1=input()
fecha2=input()