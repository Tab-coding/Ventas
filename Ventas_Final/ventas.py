import os
from datetime import datetime
import pyfiglet
os.system("cls")

#Recibe un archivo.txt y luego carga los valores en la lista libros
def cargar_productos(archivo):
    if len(libros)==0:
        with open(archivo,'r', encoding='utf-8') as file:
            for linea in file:
                linea=linea.strip()
                datos=linea.split(',')
                
                libros.append([datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],int(datos[8]),int(datos[9])])
    else:
        return -1   #Ya existen valores en la lista libros

#Recibe un archivo.txt y luego carga los valores en la lista ventas
def cargar_ventas(archivo):
    if len(ventas)==0:
        with open(archivo,'r', encoding='utf-8') as file:
            for linea in file:
                linea=linea.strip()
                datos=linea.split(',')
                
                ventas.append([int(datos[0]),datos[1],datos[2],int(datos[3]),int(datos[4])])
    else:
        return -1   #Ya existen valores en la lista ventas

#Guarda los datos de libros modificados en un archivo.txt
def respaldar_productos(lista_libros, archivo):
    with open(archivo, 'w', encoding='utf-8') as file:
        ultima_linea=len(lista_libros)
        c=1
        for linea in lista_libros:
            if c!=ultima_linea:
                file.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]},{linea[9]}\n") 
            else:
                file.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]},{linea[6]},{linea[7]},{linea[8]},{linea[9]}")  
            c=c+1
    return 1    #datos agregados

#Guarda los datos de ventas modificados en un archivo.txt
def respaldar_ventas(lista_ventas, archivo):
    with open(archivo, 'w', encoding='utf-8') as file:
        ultima_linea=len(lista_ventas)
        c=1
        for linea in lista_ventas:
            if c!=ultima_linea:
                file.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]}\n") 
            else:
                file.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]}")
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

#Genera una presentación al inicio del programa
def generar_saludo():
    print(pyfiglet.figlet_format("Sistema de Libros",justify="center"))
    print("Autor: Sebastián Loncón Araya\n")
    
#Genera una despedida para el fin del programa
def generar_despedida():
    print(pyfiglet.figlet_format("Fin del Programa.",justify="center",font="doom"))
    #print("Autor: Sebastián Loncón Araya\n")

#Recibe el input id del usuario y válida el formato.
def validar_id(id_producto):
    os.system("cls")
    if len(id_producto)==4: #El id fue bien ingresado
        if id_producto[0]=="l": #Válida el formato del id sea l001 y no p001
            return 1
        else:
            print("Recuerda que el formato del id es EJ: l001 o l002 o l003, etc...\n")
            #os.system("pause")
            return -1   #Mal formato
    else:
        print("Id en formato incorrecto.\n")
        #os.system("pause")
        return -1   #El id fue mal ingresado

#Se válida si la opción del usuario corresponde a SI,si,s o NO,no,n
#caso contrario retorna -1
def validar_opcion(op):
    if op.lower()=="si" or op.lower()=="no" or op.lower()=="s" or op.lower()=="n":
        return 1    #Formato correcto
    return -1

#Sirve para comprobar si el año es bisiesto o no
def año_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        #print("Es bisiesto")
        return 1
    else:
        #print("No es bisiesto")
        return -1

#Se válida que la fecha ingresada por el usuario, tenga buen formato
#y corresponda a una fecha verdadera
def validar_fecha(fecha):
    if len(fecha)==10:
        #dd-mm-aaaa
        if fecha[2]=='-' and fecha[5]=="-":
            try:
                dia=int(fecha[:2])
                mes=int(fecha[3:5])
                año=int(fecha[6:])
            except ValueError:
                print("Error de formato fecha...\n")
                return -1
            else:
                if año>2000:
                    bisiesto=año_bisiesto(año)
                    if mes >=1 and mes<=12:     #Verifica que el mes se encuentre entre ENERO y DICIEMBRE
                        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:    #Meses con 31 días
                            if dia>=1 and dia <=31:
                                return 1 #Formato de fecha correcto
                            else:
                                print("Día ingresado no existe\n")
                                return -1
                        elif mes==2: #Febrero
                            if bisiesto==1: # es bisiesto, entonces 29 días
                                if dia>=1 and dia<=29:
                                    return 1    #Formato de fecha correcto
                                else:
                                    print("Día ingresado no existe\n")
                                    return -1
                            else:   #no es bisiesto, entonces 28 días
                                if dia>=1 and dia<=28:
                                    return 1    #Formato de fecha correcto
                                else:
                                    print("Día ingresado no existe\n")
                                    return -1
                        else:   #Resto de meses con 30 días
                            if dia>=0 and dia<=30:
                                return 1
                            else:
                                print("Día ingresado no existe\n")
                                return -1
                    else:
                        print("Mes ingresado no existe\n")
                        return -1
                else:
                    print("Año ingresado no válido...\n")
                    return -1
        else:
            print("Recuerda que el formato es de la forma: dd-mm-aaaa")
            return -1
    else:
        print("Largo incorrecto para la fecha de formato dd-mm-aaaa")
        return -1

#Se reciben inputs del usuario con datos de libros.
#con el fin de checkear que los datos no sean vacíos o mayor a 0
def check_mant_inputs(tit, aut, edi, año, idi, cat, tipo, stock, precio):
    os.system("cls")
    if not tit:
        print("Titulo no puede ser vacío.")

    if not aut:
        print("Autor no puede ser vacío.")

    if not edi:
        print("Editorial no puede ser vacío.")

    if not año:
        print("Año no puede ser vacío.")

    if not idi:
        print("Idioma no puede ser vacío.")

    if not cat:
        print("Categoría no puede ser vacío.")

    if not tipo:
        print("Tipo no puede ser vacío.")

    if stock < 0:
        print("Stock no puede ser negativo.")

    if precio < 0:
        print("Precio no puede ser negativo.")

    if len(tit)!=0 and len(aut)!=0 and len(edi)!=0 and len(año)!=0 and len(idi)!=0 and len(cat)!=0 and len(tipo)!=0 and stock>=0 and precio>=0:
        return 1 #Pasó todas las pruebas
    else:
        return -1 #Debe ingresar nuevamente los datos

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
    try:
        opcion=int(input("Ingrese su opción: "))
        if opcion>5 or opcion<1:
            opcion=0
            print("Error, valores deben ser entre 1-5\n")
            os.system("pause")
            continue
    except ValueError:
        os.system("cls")
        print("Opción inválida, recuerda ingresar valores enteros")
        os.system("pause")
    else:   
        match opcion:
            case 1:         #VENDER LIBROS
                os.system("cls")
                if len(libros)!=0:
                    #op=""
                    while True:
                        os.system("cls")
                        cod_producto=input("Ingrese el código del producto que desea comprar: ")
                        formato=validar_id(cod_producto)
                        if formato==1:  #El id tiene buen formato (len =4 y parte con l)
                            cantidad=0
                            i=buscar_id(cod_producto)
                            if i!=-1:   #Encontró el id
                                print(libros[i][0]," ",libros[i][1]," ",libros[i][2],libros[i][3]," ",libros[i][4]," ",libros[i][5],libros[i][6]," ",libros[i][7]," ",libros[i][8],libros[i][9])
                                try:
                                    cantidad=int(input("¿Cuantos desea?: "))
                                except ValueError:
                                    print("Recuerda que debe ser un valor entero\n")
                                    os.system("pause")
                                else:
                                    if cantidad>0:
                                        if cantidad<=libros[i][8]:  #Verificar stock
                                            os.system("cls")
                                            print("STOCK DISPONIBLE!\n")
                                            total=cantidad*libros[i][9]
                                            print(f"El total a pagar es {total} \n")
                                            aux=input("Desea comprar (si/no): ")
                                            v_op=validar_opcion(aux)    #Retorna 1 si es si,s,no,n
                                            if v_op==1: #La opción es válida
                                                if aux.lower()=="si" or aux.lower()=="s":
                                                    valor_folio=rescatar_folio()+1
                                                    fecha=fecha_actual()
                                                    id_libro=libros[i][0]
                                                    ventas.append([valor_folio,fecha,id_libro,cantidad,total])
                                                    
                                                    nuevo_stock=libros[i][8]-cantidad
                                                    libros[i][8]=nuevo_stock
                                                    print("Libro comprado! \n")
                                                    
                                                    op=input("Desea comprar otro libro, (si/no): ")
                                                    v2_op=validar_opcion(op)
                                                    if v2_op==1:    #opcion entregada es valida (si,s,n,no)
                                                        if op.lower()=="no" or op.lower()=="n":
                                                            break   #No deseamos comprar más, entonces salimos
                                                    else:
                                                        print("Opción ingresada no es válida.\n")
                                                else:
                                                    op=input("Desea seguir comprando libros, (si/no): ")
                                                    v2_op=validar_opcion(op)
                                                    if v2_op==1:
                                                        if op.lower()=="no" or op.lower()=="n":
                                                            break   #No deseamos comprar más, entonces salimos
                                                    else:
                                                        print("Opción ingresada no es válida.\n")
                                            else:
                                                print("Opción ingresada no es válida.\n")
                                        else:
                                            print(f"Stock solicitado no disponible, quedan {libros[i][8]} libros en stock")
                                            n_op=input("Desea seguir comprando libros, (si/no): ")
                                            v3_op=validar_opcion(n_op)
                                            if v3_op==1:
                                                if n_op.lower()=="no" or n_op.lower()=="n":
                                                    break   #No deseamos comprar más, entonces salimos
                                            else:
                                                print("Opción ingresada no es válida.\n")
                                        os.system("pause")
                                    else:
                                        print("La cantidad a comprar debe ser mayor a 0.")
                                        os.system("pause")
                            else:
                                print("El producto no existe, ingrese nuevamente...")
                                os.system("pause")
                        else:
                            os.system("pause")
                else:
                    print("Lo sentimos, de momento no existen libros en venta.\n")
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
                            4. Salir
                        """)
                    try:
                        op=int(input("Ingrese su opción: "))
                    except ValueError:
                        print("Error, debes ingresar valores enteros.")
                        os.system("pause")
                    else: 
                        match op:
                            case 1: #Reporte General de ventas
                                os.system("cls")
                                print("--General de Ventas--")
                                total=0
                                if len(ventas)!=0:
                                    for venta in ventas:
                                        total+=venta[3]*venta[4]    #cantidad x precio
                                        print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                                    print(f"\nEl total de las ventas es, ${total}")
                                else:
                                    print("No se registran ventas...")
                                os.system("pause")
                                
                            case 2: #Reporte Ventas por fecha específica
                                os.system("cls")
                                print("--Ventas por fecha en específica--")
                                total=0
                                fecha=input("Ingrese fecha en específico (dd-mm-aaaa): ")
                                valid=validar_fecha(fecha)
                                if valid==1:
                                    for venta in ventas:
                                        if venta[1]==fecha:
                                            total+=venta[3]*venta[4]    #cantidad x precio
                                            print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                                    if total!=0:
                                        print(f"\nEl total de las ventas es, ${total}")
                                    else:
                                        print("No se registran ventas para la fecha entregada...")
                                else:
                                    print("Formato de fecha incorrecta...\n")
                                os.system("pause")
                                
                            case 3: #Reporte Venta por rango de fechas
                                os.system("cls")
                                print("--Ventas por rango de fecha--")
                                total=0
                                fecha=input("Ingrese primera fecha: ")
                                fecha2=input("Ingrese la segunda fecha: ")
                                valid=validar_fecha(fecha)
                                valid2=validar_fecha(fecha2)
                                if valid==1 and valid2==1:
                                    fecha_inicio=datetime.strptime(fecha,"%d-%m-%Y")
                                    fecha_fin=datetime.strptime(fecha2,"%d-%m-%Y")
                                    for venta in ventas:
                                        fecha_venta=datetime.strptime(venta[1],"%d-%m-%Y")
                                        if  fecha_inicio <= fecha_venta <= fecha_fin:
                                            total+=venta[3]*venta[4]     #cantidad x precio
                                            print(venta[0], " ",venta[1], " ",venta[2]," ",venta[3]," ",venta[4])
                                            
                                    if total!=0:
                                        print(f"\nEl total de las ventas es, ${total}")
                                        os.system("pause")
                                    else:
                                        os.system("cls")
                                        print("No se registran ventas para el rango de fechas...")
                                        os.system("pause")
                                else:
                                    print("Formato de fecha incorecto, intenta nuevamente")
                                    os.system("pause")
                            case 4:
                                break   #Regresar al menú principal
                            case _:
                                print("Recuerda ingresar valores entre 1-4.")
                                os.system("pause")
                        
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
                    try:
                        op=int(input("Ingrese su opción: "))
                    except ValueError:
                        os.system("cls")
                        print("Recuerda ingresar un valor entero.\n")
                        os.system("pause")
                    else:  
                        if op>=1 and op<=6:
                            os.system("cls")
                            match op:
                                case 1: #Agregar libro
                                    print("-----Agregar libro-----")
                                    id=input("Ingrese el id: ")
                                    id_formato=validar_id(id)
                                    id_existe=buscar_id(id)
                                    if id_formato == 1 and id_existe==-1: #El formato de id es correcto y el id no existe
                                        try:
                                            os.system("cls")
                                            titulo=input("Ingrese el titulo: ")
                                            autor=input("Ingrese el autor: ")
                                            editorial=input("Ingrese la editorial: ")
                                            año=input("Ingrese el año: ")
                                            idioma=input("Ingrese el idioma: ")
                                            categoria=input("Ingrese la categoria: ")
                                            tipo_tapa=input("Ingrese el tipo de tapa: ")
                                            stock=int(input("Ingrese el stock: "))
                                            precio=int(input("Ingrese el precio: "))
                                            
                                            check=check_mant_inputs(titulo,autor,editorial,año,idioma,categoria,tipo_tapa,stock,precio)
                                            if check==1:    #Pasó todos los checkeos correctamente
                                                libros.append([id,titulo,autor,editorial,año,idioma,categoria,tipo_tapa,stock,precio])
                                            else:
                                                print("\nIntente nuevamente")
                                                os.system("pause")
                                                
                                        except ValueError:
                                            print("Recuerda ingresar valores enteros para stock y precio...")
                                            os.system("pause")
                                    else:   #Formato id incorrecto o id existente
                                        #os.system("cls")
                                        print("No es posible agregar el libro")
                                        if id_existe==1:
                                            print("No es posible agregar el libro, ya existe")
                                            os.system("pause")
                                        if id_formato==-1:
                                            print("No es posible agregar el libro")
                                            os.system("pause")
                                        
                                    
                                case 2: #Buscar libro
                                    print("-----Buscar libro-----")
                                    id=input("Ingrese el id a buscar: ")
                                    i=buscar_id(id)
                                    id_formato=validar_id(id)
                                    if i!=-1 and id_formato==1: #El libro existe y el input está en el formato correcto
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
                                    id_formato=validar_id(id)
                                    if i!=-1 and id_formato==1: #El libro existe y el input está en el formato correcto
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
                                    id_formato=validar_id(id)
                                    if i!=-1 and id_formato==1: #El libro existe y el input está en el formato correcto
                                        print(f"Libro encontrado en el indice {i}")
                                        print(libros[i][0]," ",libros[i][1]," ",libros[i][2],libros[i][3]," ",libros[i][4]," ",libros[i][5],libros[i][6]," ",libros[i][7]," ",libros[i][8],libros[i][9])
                                        
                                        print("\n")
                                        try:
                                            n_titulo=input("Ingrese el titulo: ")
                                            n_autor=input("Ingrese el autor: ")
                                            n_editorial=input("Ingrese la editorial: ")
                                            n_año=input("Ingrese el año: ")
                                            n_idioma=input("Ingrese el idioma: ")
                                            n_categoria=input("Ingrese la categoria: ")
                                            n_tipo_tapa=input("Ingrese el tipo de tapa: ")
                                            n_stock=int(input("Ingrese el stock: "))
                                            n_precio=int(input("Ingrese el precio: "))
                                            check=check_mant_inputs(n_titulo,n_autor,n_editorial,n_año,n_idioma,n_categoria,n_tipo_tapa,n_stock,n_precio)
                                            
                                            if check==1:
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
                                                print("\nIntente nuevamente")
                                                os.system("pause")
                                        except ValueError:
                                            print("Error, stock y precio deben ser enteros")

                                    else:
                                        print("Error, el libro no existe")
                                        os.system("pause")
                                        
                                case 5: #Listar libros
                                    print("-----Listar libros-----")
                                    for lid,tit,au,edi,añ,idi,cat,tip,sto,pre in libros:
                                        print(lid," ",tit," ",au," ",edi," ",añ," ",idi," ",cat," ",tip," ",sto," ",pre)
                                    if len(libros)==0:
                                        print("No existen libros para listar...\n")
                                    os.system("pause")
                                    
                                case 6:break    #Regresar al menú principal
                        else:
                            print("Error, debe ingresar un valor entre 1 y 6\n")
                            os.system("pause")
            case 4:
                os.system("cls")
                op=0
                print("""
                                        MENÚ ADMINISTRACIÓN
                        1-Cargar datos
                        2-Respaldar datos
                        3-Salir
                        """)
                try:
                    op=int(input("Ingrese su opción: "))
                except ValueError:
                    print("Error, debes ingresar valores enteros.")
                    os.system("pause")
                else:
                    os.system("cls")
                    match op:
                        case 1:
                            print("Cargando datos...\n")
                            aux=cargar_productos(archivo_prod)
                            if aux==-1:
                                print("Los datos de libros ya existen")
                                #os.system("pause")
                            else:
                                #print(libros)
                                print("Datos de libros cargados con éxito!!")
                            
                            aux2=cargar_ventas(archivo_ventas)
                            if aux2==-1:
                                print("Los datos de venta ya existen")
                                #os.system("pause")
                            else:
                                #print(ventas)
                                print("Datos de ventas cargados con éxito!!")
                            os.system("pause")
                                
                        case 2:
                            if len(libros)==0 and len(ventas)==0:
                                print("No existen datos para respaldar")
                                os.system("pause")
                            else:
                                print("Respaldando datos...\n")
                                respaldar_productos(libros,archivo_prod)
                                respaldar_ventas(ventas,archivo_ventas)
                                print("Datos guardados correctamente!.\n")
                                os.system("pause")
                        case 3:continue    #Regresar al menú principal
                        case _:
                            print("Recuerda ingresar valores entre 1-3.")
                            os.system("pause")
            case 5:break    #Fin del programa

os.system("cls")
generar_despedida()