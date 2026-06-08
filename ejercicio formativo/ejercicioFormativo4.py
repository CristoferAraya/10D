import funciones as fn
nombre_usuario={}
nombre ={}
sexo={}
contraseña={}

while True:

 print("--MENU PRINCIPAL--")
 print("1.Ingresar usuario")
 print("2.Buscar usuario.")
 print("3.Eliminar usuario.")
 print("4.Salir.")

 while True:
        try:
            op = int(input("Seleccione una opcion :"))
            break
        except ValueError:
            print("Debe ingresar un valor entre 1 y 4, intente nuevamente")
    
 if op == 1:
      fn.ingrese_usuario(nombre)
 elif op == 2:
      fn.buscar_usuario(nombre)
 elif op == 3:
  fn.eliminar_usuario(nombre)
 elif op == 4:
   break
 else:  
  print("Opcion invalida,intente nuevamente")
    






