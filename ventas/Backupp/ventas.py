import os
from datetime import datetime
os.system("cls")

libros=[#id    titulo   autor   editorial  año   idioma   categoria  tipo_tapa   stock   precio       
    ["l001","Harry Potter y el Misterio del principe","J. K. Rowling","Salamandra","2022","Español","Fantasía","Tapa Dura",100,12500],
    ["l002","Tan Poca Vida","Hanya Yanagihara","Lumen Press","2016","Español","Ficción Moderna y Contemporánea","Tapa Blanda",200,27040],
    ["l003","Alas de Hierro","Rebecca Yarros","Editorial Planeta","2024","Español","Fantasía Romántica","Tapa Blanda",68,17490],
    ["l004","El Secreto de la Asistenta","Freida McFadden","SUMA","2024","Español","Ficción Literaria","Tapa Blanda",68,17490],
    ["l005","Una Corte de Rosas y Espinas","Sarah J. Maas","Crossbooks","2024","Español","Ficción","Tapa Dura",70,26940],
    ["l006","La Teoria del Amor","Ali Hazelwood","Contraluz","-","Español","Literatura Juvenil","Tapa Blanda",10,16240],
    ["l007","Lascivia","Eva Muñoz","Montena","2022","Español","Ficción Erótica","Tapa Blanda",1,19130],
    ["l008","Never lie","Freida McFadden","Dorling Kindersley Ltd.","-","Inglés","-","Tapa Blanda",3,15740],
    ["l009","Los Siete Maridos de Evelyn Hugo","Taylor Jenkins Reid","Umbriel Editores","2017","Español","Ficción Histórica","Tapa Blanda",70,12290],
    ["l010","Las Claves Secretas de Shakespeare","Carlos Basso","Penguin Random","2024","Español","THRILLER","Tapa Blanda",30,11700]]

ventas=[ #folio,    fecha,  id, cantidad,   total
    [10001,"10-06-2024","l001",2,25000],
    [10002,"10-06-2024","l002",3,81120],
    [10003,"11-06-2024","l003",6,104940],
    [10004,"11-06-2024","l004",4,69960],
    [10005,"12-06-2024","l005",10,269400],
    [10006,"12-06-2024","l006",20,324800],
    [10007,"13-06-2024","l007",1,19130],
    [10008,"13-06-2024","l008",7,110180]]


#Recibe un id de libro y retorna el índice en donde se encuentra de la lista libros.
#    -Sí no existe el id en la lista, retorna -1
def buscar_id(id_libro):
    i=0
    for libro in libros:
        if libro[0]==id_libro:
            return i
        i+=1
    return -1

#Rescata el valor del ultimo folio en la lista de ventas. 
def rescatar_folio():
    folio=ventas[-1][0]  #ultimo folio1
    return folio

#Entrega la fecha actual del modo: día-mes-año
def fecha_actual():
    date =datetime.now()
    day_month_year=date.strftime("%d-%m-%Y")
    return day_month_year

#-----------MAIN------------
opcion=0
while opcion<=4:
    os.system("cls")
    print("""
                 Sistema de ventas
            ---------------------------
            1.Vender libros
            2.Reportes
            3.Mantenedores
            4.Administración
            5.Salir
        """)
    opcion=int(input("Ingrese su opción: "))
    match opcion:
        case 1:         #VENDER LIBROS
            op="si"
            while op.lower()=="si":
                os.system("cls")
                cod_producto=input("Ingrese el código del producto que desea comprar: ")
                cantidad=0
                i=buscar_id(cod_producto)
                if i!=-1:
                    print(libros[i][0]," ",libros[i][1]," ",libros[i][2],libros[i][3]," ",libros[i][4]," ",libros[i][5],libros[i][6]," ",libros[i][7]," ",libros[i][8],libros[i][9])
                    cantidad=int(input("¿Cuantos desea?: "))
                    if cantidad<=libros[i][8]:  #Verificar stock
                        print("STOCK DISPONIBLE!\n")
                        total=cantidad*libros[i][9]
                        print(f"El total a pagar es {total} \n")
                        aux=input("Desea comprar (si/no): ")
                        if aux.lower()=="si":
                            valor_folio=rescatar_folio()+1
                            fecha=fecha_actual()
                            id_libro=libros[i][0]
                            ventas.append([valor_folio,fecha,id_libro,cantidad,total])
                            
                            nuevo_stock=libros[i][8]-cantidad
                            libros[i][8]=nuevo_stock
                            print("Libro comprado! \n")
                            
                            op=input("Desea comprar otro libro, (si/no): ")
                        else:
                            op=input("Desea comprar otro libro, (si/no): ")
                    else:
                        print(f"Stock solicitado no disponible, solo quedan {libros[i][8]} libros en stock")
                    os.system("pause")
                else:
                    print("El producto no existe, ingrese nuevamente...")
                    os.system("pause")
            
        case 2:         #REPORTES
            os.system("cls")
            op=0
            while op<=4:
                os.system("cls")
                print("""
                            Reportes
                        ------------------------
                        1. General de ventas (con total)
                        2. Ventas por fecha específica (con total)
                        3. Ventas por rango de fecha (con total)
                        4.Salir
                    """)
                op=int(input("Ingrese su opción: "))
                
                match op:
                    case 1: #Reporte General de ventas
                        os.system("cls")
                        print("--General de Ventas--")
                        total=0
                        for venta in ventas:
                            total+=venta[3]*venta[4]    #cantidad x precio
                            print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                        print(f"\nEl total de las ventas es, ${total}")
                        os.system("pause")
                        
                    case 2: #Reporte Ventas por fecha específica
                        os.system("cls")
                        print("--Ventas por fecha en específica--")
                        total=0
                        fecha=input("Ingrese fecha en específico: ")
                        for venta in ventas:
                            if venta[1]==fecha:
                                total+=venta[3]*venta[4]    #cantidad x precio
                                print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                        if total!=0:
                            print(f"\nEl total de las ventas es, ${total}")
                        else:
                            print("No se registran ventas para la fecha entregada...")
                        os.system("pause")
                        
                    case 3: #Reprote Venta por rango de fechas
                        os.system("cls")
                        print("--Ventas por rango de fecha--")
                        total=0
                        fecha=input("Ingrese primera fecha: ")
                        fecha2=input("Ingrese la segunda fecha: ")
                        for venta in ventas:
                            if  venta[1]>=fecha and venta[1]<=fecha2:
                                total+=venta[3]*venta[4]     #cantidad x precio
                                print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                                
                        if total!=0:
                            print(f"\nEl total de las ventas es, ${total}")
                        else:
                            print("No se registran ventas para el rango de fechas...")
                        os.system("pause")
                    case 4:
                        break   #Regresar al menú principal
                    
        case 3:         #MANTENEDORES
            op=0
            while op<=6:
                os.system("cls")
                print("""
                    -----CRUD--------
                    1-Agregar libro
                    2-Buscar libro
                    3-Eliminar libro
                    4-Modificar libro
                    5-Listar libros
                    6-Regresar al Sistema de ventas
                    """)
                op=int(input("Ingrese su opción: "))
                if op>=1 and op<=6:
                    match op:
                        case 1: #Agregar libro
                            print("-----Agregar libro-----")
                            id=input("Ingrese el id: ")
                            titulo=input("Ingrese el titulo: ")
                            autor=input("Ingrese el autor: ")
                            editorial=input("Ingrese la editorial: ")
                            año=input("Ingrese el año: ")
                            idioma=input("Ingrese el idioma: ")
                            categoria=input("Ingrese la categoria: ")
                            tipo_tapa=input("Ingrese el tipo de tapa: ")
                            stock=int(input("Ingrese el stock: "))
                            precio=int(input("Ingrese el precio: "))
                            libros.append([id,titulo,autor,editorial,año,idioma,categoria,tipo_tapa,stock,precio])
                            os.system("pause")
                            
                        case 2: #Buscar libro
                            print("-----Buscar libro-----")
                            id=input("Ingrese el id a buscar: ")
                            i=buscar_id(id)
                            if i!=-1:
                                os.system("cls")
                                print(f"Libro encontrado en el indice {i}")
                                print(libros[i][0]," ",libros[i][1]," ",libros[i][2],libros[i][3]," ",libros[i][4]," ",libros[i][5],libros[i][6]," ",libros[i][7]," ",libros[i][8],libros[i][9])
                                os.system("pause")
                            else:
                                print("Error, el libro no existe")
                                os.system("pause")
                                
                        case 3: #Eliminar libro
                            print("-----Eliminar libro-----")
                            id=input("Ingrese el id a buscar: ")
                            i=buscar_id(id)
                            if i!=-1:
                                os.system("cls")
                                print(f"Libro encontrado en el indice {i}")
                                libros.pop(i)
                                print("Listo, libro eliminado")
                                os.system("pause")
                            else:
                                print("Error, el libro no existe")
                                os.system("pause")
                                
                        case 4: #Modificar libro
                            print("-----Modificar libro-----")
                            id=input("Ingrese el id a buscar: ")
                            i=buscar_id(id)
                            if i!=-1:
                                print(f"Libro encontrado en el indice {i}")
                                print(libros[i][0]," ",libros[i][1]," ",libros[i][2],libros[i][3]," ",libros[i][4]," ",libros[i][5],libros[i][6]," ",libros[i][7]," ",libros[i][8],libros[i][9])
                                
                                print("\n")
                                n_titulo=input("Ingrese el titulo: ")
                                n_autor=input("Ingrese el autor: ")
                                n_editorial=input("Ingrese la editorial: ")
                                n_año=input("Ingrese el año: ")
                                n_idioma=input("Ingrese el idioma: ")
                                n_categoria=input("Ingrese la categoria: ")
                                n_tipo_tapa=input("Ingrese el tipo de tapa: ")
                                n_stock=int(input("Ingrese el stock: "))
                                n_precio=int(input("Ingrese el precio: "))

                                libros[i][1]=n_titulo
                                libros[i][2]=n_autor
                                libros[i][3]=n_editorial
                                libros[i][4]=n_año
                                libros[i][5]=n_idioma
                                libros[i][6]=n_categoria
                                libros[i][7]=n_tipo_tapa
                                libros[i][8]=n_stock
                                libros[i][9]=n_precio
                                os.system("cls")
                                print("Listo, libro modificado")
                                os.system("pause")
                            else:
                                print("Error, el libro no existe")
                                os.system("pause")
                                
                        case 5: #Listar libros
                            print("-----Listar libros-----")
                            for lid,tit,au,edi,añ,idi,cat,tip,sto,pre in libros:
                                print(lid," ",tit," ",au," ",edi," ",añ," ",idi," ",cat," ",tip," ",sto," ",pre)
                            os.system("pause")
                            
                        case 6:break    #Regresar al menú principal
            else:
                print("Error, debe ingresar un valor entre 1 y 6")
        case 4:break    #Fin del programa