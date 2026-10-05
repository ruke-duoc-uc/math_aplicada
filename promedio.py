def ingresar_nota(origen,porcentaje=None):
    while True:
        try:
            if origen == "usuario":
                nota = int(input(f"Ingrese la nota ({porcentaje}%)\n: "))
                if 10 <= nota <= 70:
                    return nota
                print("La nota debe estar entre 10 y 70")
            elif origen == "lista_notas":
                lista_notas = []
                for i in range(len(porcentaje)):
                    while True:
                        try:
                            nota = int(input(f"Ingrese la nota ({porcentaje[i]}%)\n: "))
                            if 10 <= nota <= 70:
                                nota_vuelta = nota*porcentaje[i]
                                lista_notas.append(nota_vuelta)
                                print(f"Valor de la nota: {nota_vuelta}")
                                break
                            print("La nota debe estar entre 10 y 70")
                        except ValueError:
                            print("La nota debe ser un número entero")
                return lista_notas
        except ValueError:
            print("Ingrese un valor valido (entero)")


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
            nota_vuelta = ingresar_nota("usuario",porcentaje) 
            print(nota_vuelta)
        print(f"Valor de la nota: {nota_vuelta*(porcentaje/100)} ")
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


def calculo_con_lista(porcentajes_materia):
    total = 0
    lista_nota = []
    lista_porcentajes = porcentajes_materia
    presentacion_parciales = 0
    try:
        lista_nota = ingresar_nota("lista_notas",lista_porcentajes)
    except ValueError:
        print("a")
# Transversal (40 porciento)
    while True:
        try:
            nota_transversal = int(input(f"Ingrese la nota (0.40%)\n: "))
            break
        except ValueError:
            print("Ingrese un valor valido (entero)")
    for i in range(len(lista_porcentajes)):
        nota_vuelta =lista_nota[i]
        total = total+nota_vuelta
        presentacion_parciales = presentacion_parciales + lista_nota[i]
        print(f"Valor de la nota: {round(nota_vuelta)}")
    total = (total*0.6) + nota_transversal*0.4
    if total > 70:
        total == 70
    print(f"Presentacion parciales (60%): {round(presentacion_parciales)}")
    print(f"Transversal (40%): {round(nota_transversal*0.4)}")
    print(f"Nota final: {round(total)}")
def opcion_1():
    while True:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de parciales\n:"))
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
    print("4) Por materia")
    print("5) Salir")
    try:
        seleccion = input("Eliga una opcion\n: ")
        if seleccion == "1":
            opcion_1()
        if seleccion == "4":
            try:
                print("Matematica Aplicada")
                print("Taller de base de datos")
                print("Desarrollo Fullstack II")
                print("Desarrollo de aplicaciones moviles")
                materia = input("Eliga una materia")
                origen = "lista_notas"
                matematicas = [0.1,0.1,0.35,0.1,0.35]
                if materia == "1":
                    calculo_con_lista(matematicas)
            except Exception as e:
                print(f"Ingrese una opción valida (numero)\n{e}")                
        elif seleccion == "5":
            print("-----PROGRAMA FINALIZADO-----")
            programa = False
    except Exception as e:
        print(f"Ingrese una opción valida (numero)\n{e}")