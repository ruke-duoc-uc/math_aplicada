# origen determina que parte de la funcion se ejecuta
# porcentaje puede ser un "int" o una lista
# Ambos atributos se lo otorgan otras funciones
def ingresar_nota(origen,porcentaje):
    while True:
        try:
            if origen == "usuario":
                nota = int(input(f"Ingrese la nota ({porcentaje}%)\n: "))
                if 10 <= nota <= 70:
                    nota_calculada = nota * (porcentaje / 100)
                    return nota_calculada
                print("La nota debe estar entre 10 y 70")
            # Fragmento dedicado a "calculo_con_lista"
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
        total = total+nota_vuelta
        lista_nota.append(nota_vuelta)
        lista_porcentajes.append(porcentaje)
    # Una vez se termine de ingresar todos los parciales, se hace ajuste 
    # de su valor, en este caso un 60%
    total = total*0.6
    while True:
        try:
            nota_transversal = int(input(f"Ingrese la nota del Transversal (40%)\n: "))
            nota_transversal = nota_transversal * 0.4
            break
        except ValueError:
            print("Ingrese un valor valido (entero)")
    print(f"Notas en orden: {lista_nota}")
    print(f"Porcentajes en orden: {lista_porcentajes}")
    print(f"Parciales: {total}")
    print(f"Tranversal: {nota_transversal}")
    print(f"Nota final: {total+nota_transversal}")
    for i in range(len(lista_nota)):
        nota_parciales = lista_nota[i]
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
            cantidad_notas = int(input("Ingrese la cantidad de parciales\n: "))
            print(cantidad_notas)
            break
        except ValueError:
            print("Ingrese un número entero")
    calculo_manual(cantidad_notas)
programa = True

while programa == True:
    print("----- CALCULO DE NOTAS -----")
    print("1) Forma libre (60% y 40%)")
    print("2) Por materia")
    print("3) Salir")
    try:
        seleccion = input("Eliga una opcion\n: ")
        if seleccion == "1":
            print("Este modulo te permitira definir cuantas notas tienes en los parciales")
            print("y cuanto porcentaje valen para la 'Nota de presentación'.")
            print("Ademas, calculara cuanto vale la Transversal")
            opcion_1()
        if seleccion == "2":
            while True:
                try:
                    print("1) Matematica Aplicada")
                    print("2) Taller de base de datos")
                    print("3) Desarrollo Fullstack II")
                    print("4) Desarrollo de aplicaciones moviles")
                    print("5) Etica para el trabajo")
                    materia = input("Eliga una materia\n: ")
                    origen = "lista_notas"
                    # Valor de porcentajes predefinido por materia
                    matematicas = [0.1,0.1,0.35,0.1,0.35]
                    base_datos = [0.3,0.4,0.3]
                    fullstackii = [0.3,0.3,0.4]
                    apps = [0.3,0.08,0.32,0.06,0.24]
                    etica = [0.35,0.35,0.3]
                    # Gracias a este diccionario evita tener que 
                    # usar la estructura if/elif ... ↓↓↓
                    acciones = {
                        "1": matematicas,
                        "2": base_datos,
                        "3": fullstackii,
                        "4": apps,
                        "5": etica
                    }
                    # resultado lee la lista tomando en cuenta la eleccion
                    # del usuario, llamando a la funcion dedicada al calculo de notas
                    # con lista
                    resultado = acciones.get(materia,[])
                    if resultado:
                        calculo_con_lista(resultado)
                        break
                    else:
                        print("Eliga una opcion valida")
                except Exception as e:
                    print(f"Ingrese una opción valida (numero)\n{e}")                
        elif seleccion == "3":
            print("-----PROGRAMA FINALIZADO-----")
            programa = False
    except Exception as e:
        print(f"Ingrese una opción valida (numero)\n{e}")