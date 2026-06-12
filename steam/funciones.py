def mostrar_menu():
    while True:
     print("1: Ver Catálogo de Tienda")
     print("2: Agregar juego al Carrito")
     print("3: Ver mi Carrito")
     print("4: Cargar fondos a la Cartera")
     print("5: Pagar Carrito")
     print("6: Ver mi Biblioteca")
     print("7: Salir")
     



def mostrar_juego(lista_generica):
   if len(lista_generica) == 0:
      print("No hay nada en la lista")