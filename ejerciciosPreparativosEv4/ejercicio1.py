'''productos = {
"Mouse": [10, 15000],
"Teclado": [5, 25000],
"Monitor": [3, 180000]
}'''

#definicion de funciones
def agregar_producto(productos):
    nombre =input("Nombre del producto: ").strip().lower()

    if nombre =="":
       print("El nombre no puede ser vacio")
       return

    if nombre in productos:
       print("El producto ya existe!")
       return

    stock = int(input("Ingrese stock :"))
    precio =int(input("Ingrese precio $ :"))

    productos[nombre] = [stock,precio]
    print("Productos agregados correctamente")



productos={}
#menu ppal
while True:
     #try:
    print("---Menu---")
    print("1.Agregar producto")
    print("2.Mostrar producto")
    print("3. Buscar productoo")
    print("4. Producto mas caro")
    print("5.Salir")
    op = input("Seleccione opcion : ")
    print(op)




    # while True:
    #    try:
    #       op =int(input("Seleccione opcion : "))
    #       break
    #    except ValueError:
    #       print("Error, debe ingresar un numero entre 1 y 5,Intente nuevamente")

    # if op == 1:
    #    #agregar_producto(productos):
    #    print("1")
    # elif op == 2:
    #     #mostrar_productos(productos):
    #     print("2")
    # elif op ==3:
    #    #buscar_producto(productos):
    #    print("3")


