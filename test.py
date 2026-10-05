def ingreso_porcentaje():
    while True:
        try:
            porcentaje = int(input(f"Ingrese el porcentaje\n: "))
            return porcentaje
        except ValueError:
            print("Ingrese un porcentaje valido (entero)")
def calculo_manual(vueltas):
    total = 0
    lista_nota = []
    lista_porcentajes = []
    for i in range(vueltas):
        lista_porcentajes.append(ingreso_porcentaje())
    print(lista_porcentajes)
while True:
    try:
        cantidad_notas = int(input("Ingrese la cantidad de parciales\n: "))
        break
    except ValueError:
        print("Ingrese un número entero")
calculo_manual(cantidad_notas)
