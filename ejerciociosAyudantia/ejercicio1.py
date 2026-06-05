def mostrar_menu():
    print("\n1.Agregar tarea")
    print("2.Eliminar tarea")
    print("3.Ver tarea")
    print("4.Salir")



def imprimir_tareas(lista_tarea):
    if len(lista_tarea) == 0:
        print("No hay tareas")
    else:
        lista_tarea.sort()
        print("tareas pendientes")
        for tarea in lista_tarea :
            print(f"-{tarea}")

tareas =[]
while True:
    mostrar_menu()
    op = input("--> :  ")
    if op == "1":
        agregar=input("\nIngresar tarea: ").strip().capitalize()
        tareas.append(agregar)
        print(f"\nTarea{agregar} agregada correctamente")
    elif op =="2":
        quitar = input("\nIngresar tarea: ").strip().capitalize()
        if quitar in tareas:
            print("Tarea eliminada")
            tareas.remove(quitar)
        else:
            print("No existe")
    elif op == "3":
        imprimir_tareas(tareas)
    elif op == "4":
        break
    else:
        print("opcion invalida.")