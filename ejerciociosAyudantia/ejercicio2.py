contactos={}

def pedir_opcion():
    op=input("[A] agregar contacto | [B] buscar contacto | [S] salir\n--> ")
    return op

def buscar_numero(agenda, nombre_buscado):
    if nombre_buscado in agenda:
        return agenda[nombre_buscado]
    else:
        return "El contacto no existe en la agenda"
    
while True:
    opcion = pedir_opcion()

    if opcion == "A":
        nombre = input("Ingresa el nombre: ").strip().title()
        numero = input("Ingrese el telefono: ").strip().title()

        contactos [nombre] = numero
        print(f"Contacto {nombre} guardado")

    elif opcion == "B":
        nombre = input("Buscando contacto: ").strip().title()

        resultado = buscar_numero(contactos, nombre)
        print(f"Resultados: {resultado}")

    elif opcion == "C":
        print("Saliendo")
        break
    else:
        print("Opcion invalidac")
