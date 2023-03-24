ARS = 202.91
COL = 4849.99
MEX = 18.74

def calculo_moneda(moneda):
    dolares = int(input("Cuantos dolares tienes: "))
    pesos = moneda * dolares
    return pesos

def ingreso_menu ():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre} Bienvenido al convertidor de monedas")
    print(" 1 - Dolares estadounidenses a pesos aregentinos")
    print(" 2 - Dolares estadounidenses a pesos colombianos")
    print(" 3 - Dolares estadounidenses a pesos mexicanos")
    opcion = int(input("Cual es la opcion que deseas: "))
    if opcion > 3:
        raise ValueError("Error solo existen tres opciones")
    return opcion

def conversion_moneda(opcion):
    if opcion == 1:
        print(f"Tienes {calculo_moneda(ARS)} pesos aregentinos")
    else:
        if opcion == 2:
                print(f"Tienes {calculo_moneda(COL)} pesos colombianos")
        else:
            if opcion == 3:
                print(f"Tienes {calculo_moneda(MEX)} pesos mexicanos")

menu=ingreso_menu()
conversion_moneda(menu)

