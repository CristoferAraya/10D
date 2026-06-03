def leer_nota(mensaje):
    while True:
        try:
            nota =float(input(mensaje))
            if nota >= 1.0 and nota <= 7.0:
                return nota 
            print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Debe ingresar una nota valida !")

def agregar_alumno(alumnos):
    nombre = input("Nombre del alumno: ").strip()

    if nombre =="":
        print("El nombre no puede estar vacio")
        return
    
    if nombre in alumnos:
        print("El alumno ya existe ")
        return
    if nombre.isdigit():
        print("El nombre debe ser letra")
        return
    
    cantidad = int(input("Cantidad de notas:{i}"))

    notas=[]

    for i in range (cantidad):
        nota = leer_nota(f"Ingrese nota {i+1}")
        notas.append(nota)

    alumnos[nombre] = notas
    print("Alumno agregado correctamente")


def mostrar_alumnos(alumnos):
    if len(alumnos)== 0:
        print("No hay alunmos registrados")
        return
    for nombre in alumnos:
        print(nombre,":",alumnos[nombre])
        
def ver_promedios(alumnos):
    if len(alumnos)== 0:
        print("No hay alunmos registrados,no se pueden ver los promedios")
        return
    
    for nombre in alumnos:
        promedio = sum(alumnos[nombre]) /len(alumnos[nombre])
        print(nombre,"Tiene un promedio de",round(promedio,1))


def mejor_alumno(alumnos):
     if len(alumnos)== 0:
        print("No hay alunmos registrados,no se pueden ver los promedios")
        return
     mejorAlumno = 0
     mejor_promedio =0
     for nombre in alumnos:
         promedio = sum(alumnos[nombre]) /len(alumnos[nombre])

         if promedio > mejor_promedio:
             mejor_promedio = promedio
             mejorAlumno = nombre
     print("Mejor alumno :",mejorAlumno,"con promedio: ",round(mejor_promedio,1))


def cantidad_aprobados(alumnos):
     if len(alumnos)== 0:
        print("No hay alunmos registrados")
        return
     aprobados=0
     for nombre in alumnos:
         promedio = sum(alumnos[nombre]) /len(alumnos[nombre])
         if promedio >= 4.0:
             promedio = aprobados + 1
     print("Cantidad de aprobados es :",aprobados)