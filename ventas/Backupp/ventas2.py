import os
from datetime import datetime
import pyfiglet
os.system("cls")

#Recibe un archivo.txt y luego carga los valores en la lista libros
def cargar_productos(archivo):
    if len(libros)==0:
        with open(archivo,'r') as file:
            for linea in file:
                linea=linea.strip()
                datos=linea.split(',')
                
                libros.append([datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],int(datos[8]),int(datos[9])])
    else:
        return -1   #Ya existen valores en la lista libros

#Recibe un archivo.txt y luego carga los valores en la lista ventas
def cargar_ventas(archivo):
    if len(ventas)==0:
        with open(archivo,'r') as file:
            for linea in file:
                linea=linea.strip()
                datos=linea.split(',')
                
                ventas.append([int(datos[0]),datos[1],datos[2],int(datos[3]),int(datos[4])])
    else:
        return -1   #Ya existen valores en la lista ventas

def respaldar_productos(lista_libros, archivo):
    with open(archivo, 'w') as file:
        ultima_linea=len(lista_libros)
        c=1
        for linea in lista_libros:
            if c!=ultima_linea:
                file.write(f"{linea[0]},{linea[1]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]},{linea[9]}\n") 
            else:
                file.write(f"{linea[0]},{linea[1]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]},{linea[9]}")  
            c=c+1
    return 1    #datos agregados

def respaldar_ventas(lista_ventas, archivo):
    with open(archivo, 'w') as file:
        ultima_linea=len(lista_ventas)
        c=1
        for linea in lista_ventas:
            if c!=ultima_linea:
                file.write(f"{linea[0]},{linea[1]},{linea[3]},{linea[4]}\n") 
            else:
                file.write(f"{linea[0]},{linea[1]},{linea[3]},{linea[4]}")
            c=c+1
    return 1    #datos agregados


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

def generar_saludo():
    print(pyfiglet.figlet_format("Sistema de Libros",justify="center"))
    print("Autor: Sebastián Loncón Araya\n")
    
#-----------MAIN------------
#Nombre de archivos
archivo_prod='productos.txt'
archivo_ventas='ventas_prod.txt'

libros=[#id    titulo   autor   editorial  año   idioma   categoria  tipo_tapa   stock   precio       
    ]

ventas=[ #folio,    fecha,  id, cantidad,   total
    ]

opcion=0
generar_saludo()
os.system("pause")

while opcion<=5:
    os.system("cls")
    print(f"""
                                                            {fecha_actual()}
                                                            versión: v02
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
        case 4:
            os.system("cls")
            op=0
            print("""
                                    MENÚ ADMINISTRACIÓN
                    1-Cargar datos
                    2-Respaldar datos
                    3-Salir
                    """)
            op=int(input("Ingrese su opción: "))
            match op:
                case 1:
                    print("Cargando datos...\n")
                    aux=cargar_productos(archivo_prod)
                    if aux==-1:
                        print("Los datos de libros ya existen")
                        os.system("pause")
                    else:
                        #print(libros)
                        print("Datos de libros cargados con éxito!!")
                    
                    aux2=cargar_ventas(archivo_ventas)
                    if aux2==-1:
                        print("Los datos de venta ya existen")
                        os.system("pause")
                    else:
                        #print(ventas)
                        print("Datos de ventas cargados con éxito!!")
                    os.system("pause")
                        
                case 2:
                    print("Respaldando datos")
                case 3:break    #Regresar al menú principal
        case 5:break    #Fin del programa