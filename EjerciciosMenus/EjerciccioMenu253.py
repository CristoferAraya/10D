menu = True
while menu :
    print("--MENU--")
    print("1. Pago Tarjeta de credito")
    print("2. Simulacion de compra")
    print("3. Salir")

    op = int(input("Ingrese su opcion"))

    if op == 1 :
        print("Pago Tarjeta de credito")
    elif op == 2 :
        print(" Comprando...")
    elif op == 3:
        print(" Saliendo")
        menu = False
    else:
        print("Opcion invalida")