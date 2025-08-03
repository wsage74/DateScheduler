def Menu():
    print("\n----MENU----\n")
    print('Si quiere registrar una cita digite "1"')
    print('Si quiere ver sus citas registradas digite "2"')      #Menú del programa
    print('Si quiere borrar alguna cita digite "3"')
    print('Salir "4"')


def RegistrarFecha(dia, mes, año, nombre):
    fecha = {"Día": dia,
            "Mes": mes,
            "Año": año,
            "Nombre": nombre}
#Acá se crea o accede al documento 'fechas.txt' y se guardan las fechas allí.
    with open("fechas.txt", "a") as archivo: 
        archivo.write(f"Nombre: {fecha["Nombre"]}, Día: {fecha["Día"]}, Mes: {fecha["Mes"]}, Año: {fecha["Año"]}\n")
    return fecha


def MostrarFecha():
    with open("fechas.txt", "r") as archivo:
        obtener = archivo.readlines()  #El metodo .readlines() convierte todas las líneas del archivo en listas.
        if not obtener:
            print("\nAún no ha registrado una cita")
            return False
        else:
            i = len(obtener)
            print(f"\n---Tienes registradas {i} cita/s---\n")
            for contador, f in enumerate(obtener, start=1):
                print(f"{contador}. {f}".strip()) #El metodo .strip() hace que se eliminen espacios al inicio y al final de la lista.


def BorrarFecha(num_Fecha):
    num_Fecha_qsevaausar = num_Fecha -1

    with open("fechas.txt", "r") as archivo:
        obtener = archivo.readlines()
        if num_Fecha_qsevaausar < 0 or num_Fecha_qsevaausar > len(obtener):
            print("No hay alguna cita registrada con ese número")
            return

        del obtener[num_Fecha_qsevaausar]
        with open("fechas.txt", "w") as archivo:
            archivo.writelines(obtener)
    print(f"\nLa cita {num_Fecha} se ha eliminado con éxito")

while True:
    Menu()
    try:
        choice = int(input("\nDigite su opción: "))
    except ValueError:
        print("\n¡Entrada invalida, digite un número entre (1-4)!")
        continue

    if choice == 1:
        try:
            dia = int(input("\nDigite el día: "))
            mes = input("Digite el nombre del mes: ")
            mes = mes.capitalize()
            año = int(input("Digite el año: "))
            nombre = input("Digite con que nombre quiere guardar la cita: ")
        except ValueError:
            print("\n¡Digite una opción valida!")
            continue
            
        if mes != "Enero" and mes != "Febrero" and mes != "Marzo" and mes != "Abril" and mes != "Mayo" and mes != "Junio" and mes != "Julio" and mes != "Agosto" and mes != "Septiembre" and mes != "Octubre" and mes != "Noviembre" and mes != "Diciembre":
            print("\n¡Error al Digitar el Mes!")
            continue

        if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
            if dia < 1 or dia > 31:
                print("\n¡Error, el mes que seleccionaste tiene entre (1-31) días!")
                continue
            else:
                pass
        elif mes == "Abril" or mes == "Junio" or mes == "Septiembre" or mes == "Noviembre":
            if dia < 1 or dia > 30:
                print("\n¡Error, el mes que seleccionaste tiene entre (1-30) días!")
                continue
        else:
            if año%4 == 0:
                if dia < 1 or dia > 29:
                    print("\n¡Error, el mes que seleccionaste tiene entre (1-29) días!, ¡¡Es año bisiesto!!")
                    continue
            else:
                if dia < 1 or dia > 28:
                    print("\n¡Error, el mes que seleccionaste tiene entre (1-28) días!")
                    continue
                else:
                    pass

        fecha_agregada = RegistrarFecha(dia, mes, año, nombre)
        print(f"\nLa fecha fue registrada {fecha_agregada}")

    elif choice == 2:
        MostrarFecha()

    elif choice == 3:
        if MostrarFecha() == False:
            continue
        try:
            num_Fecha = int(input("\nDigite el número de la cita que desea eliminar: "))
        except ValueError:
            print("\n!Entrada Invalida¡ repita el proceso")
            continue
        BorrarFecha(num_Fecha)
        
    elif choice == 4:
        print("\nSee you next time (╥﹏╥)\n")
        break