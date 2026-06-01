'''productos = {
    "Mouse": [10, 15000],
    "Teclado": [5, 25000],
    "Monitor": [3, 180000]
}'''
#definicion de funciones
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre .isdigit():
        print("Debe ingresar letra!!!")
        return





    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    if nombre in productos:
        print("El producto ya existe!")
        return
    
    while True:
          try:
              stock = int(input("Ingrese stock"))
              break
          except ValueError:
              print()
 

    while True:
        try:
    
         precio = int(input("Ingrese precio $:"))
         break
        except ValueError:
         print("Debe ingresar un numero para el precio!!!, vuelva a intentar")

 

    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente!")

def mostrar_productos(productos):
    if len(productos)== 0:
        print("No existen preoductos")
        return
    
    for nombre in productos:
        print(nombre,"--Stock :",productos[nombre][0],"--Precio :$",productos[nombre][1])


def buscar_productos(productos):
    if len(productos)== 0:
        print("No existen productos")
        return
    
    nombre = input("Nombre producto a buscar :").strip()

    if nombre in productos:
        print("Producto encontrado")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio :$ {productos[nombre][1]}")
    else:
        print("Producto no existe o agotado")


def producto_mas_caro(productos):
    if len (productos)==0:
        print("No existen productos")
        return
    mayor = 0
    mayorNombre = ""
    for nombre in productos:
        precio =productos[nombre][1]



productos={}
#menu ppal
while True:
    print("---MENU---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Producto mas caro")
    print("5. Salir")

    while True:
        try:
            op = int(input("Selecccione opción: "))
            break
        except ValueError:
            print("Error, debe ingresar un número entre 1 y 5, Intente Nuevamente")

    if op == 1 :
        agregar_producto(productos)

        
    elif op == 2:
        #mostrar_productos(productos)
        print(productos)
        
    elif op == 3:
        #buscar_producto(productos)
        print("3")
        
    elif op == 4:
        #poducto_mas_caro(productos)
        print("4")
    elif op == 5:
        print("Fin del programa...")
        break
    else:
        print("Opción inválida!")
    