def ponderar(nota,porcentaje):
    return print(f"Valor de la nota{(nota*porcentaje)/100} ")

def programa_completo():
    cantidad_notas = int(input("Ingrese la cantidad de parciales\n:"))
    for i in range(cantidad_notas):
        try:
            porcentaje = int(input(f"Ingrese el porcentaje"))
        except:
            print("Ingrese un valor valido (entero)")
        try:
            nota = int(input(f"Ingrese la nota"))
        except:
            print("Ingrese un valor valido (entero)")
        ponderar(nota,porcentaje)
programa = True

while programa == True:
    print("----- CALCULO DE NOTAS -----")
    print("1) Parciales y Transversal")
    print("2) Solo parciales")
    print("3) Solo Transversal")
    print("4) Salir")
    seleccion = input("Eliga una opcion\n:")
    if seleccion == "1":
        programa_completo()
    elif seleccion == "4":
        print("-----PROGRAMA FINALIZADO-----")
        programa = False
    else:
        print("Ingrese el numero de la opción que quiera")