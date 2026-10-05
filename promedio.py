def calculo_manual(vueltas):
    total = 0
    lista_nota = []
    lista_porcentajes = []
    for i in range(vueltas):
        while True:
            try:
                porcentaje = int(input(f"Ingrese el porcentaje\n: "))
                break
            except ValueError:
                print("Ingrese un porcentaje valido (entero)")
        while True:
            try:
                nota = int(input(f"Ingrese la nota ({porcentaje}%)\n: "))
                if 10 <= nota <= 70:
                    break
                print("La nota debe estar entre 10 y 70")
            except ValueError:
                print("Ingrese un valor valido (entero)")
        print(f"Valor de la nota: {nota*(porcentaje/100)} ")
        total = total+(nota*porcentaje)/100
        lista_nota.append(nota)
        lista_porcentajes.append(porcentaje)
    while True:
        try:
            nota_transversal = int(input(f"Ingrese la nota\n: "))
            break
        except ValueError:
            print("Ingrese un valor valido (entero)")
    print(f"Nota final: {total+(nota_transversal*0.40)}")
    print(f"Notas en orden: {lista_nota}")
    print(f"Porcentajes en orden: {lista_porcentajes}")
    print(f"Parcial: {nota_transversal}")
    for i in range(len(lista_nota)):
        nota_parciales = nota_parciales = lista_nota[i]
        print(lista_nota[i])
def opcion_1():
    while True:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de parciales\n: "))
            break
        except ValueError:
            print("Ingrese un número entero")
    calculo_manual(cantidad_notas)
    
programa = True

while programa == True:
    print("----- CALCULO DE NOTAS -----")
    print("1) Parciales y Transversal")
    print("2) Solo parciales")
    print("3) Solo Transversal")
    print("4) Salir")
    try:
        seleccion = input("Eliga una opcion\n:")
        if seleccion == "1":
            opcion_1()
        elif seleccion == "4":
            print("-----PROGRAMA FINALIZADO-----")
            programa = False
    except Exception as e:
        print(f"Ingrese una opción valida (numero)\n{e}")