def ingrese_usuario(nombre_usuario):
    nombre= input("Ingrese nombre : ").strip()

    if nombre =="":
        print("El nombre no puede esta vacio")
        return
    
    if nombre in nombre_usuario:
        print("El usuario ya existe")
        return
    if nombre.isdigit():
        print("El nombre debe ser letra")
        return
    
    contraseña=int(input("Ingrese conraseña"))
    if contraseña=="":
     print("Este campo no puede estar vacio")

    sexo=input("Ingrese su sexo")
    if sexo=="":
     print("Este campo no puede estar vacio")

def buscar_usuario(nombre_usuario):
   if len(nombre_usuario) == 0:
      print("NO hay usuarios registrados")
      return
   
   for nombre in nombre_usuario:
      print(nombre,":",nombre_usuario[nombre]) 


def eliminar_usuario(nombre_usuario):
   if len(nombre_usuario)==0:
      print("No exixten usuarios")
eliminar_usuario=int(input("Ingrese usuario :"))