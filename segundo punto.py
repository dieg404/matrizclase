estudiantes = [
    ["Estudiantes", "Examen 1", "Examen 2", "Tarea 1", "Tarea 2", "Proyecto"]
]

# Función de bucle para agregar los estudiantes y sus notas
def notas():
    global x, pf, e
    while x <= c:
        e = input(f"Ingrese el nombre del estudiante número {x}: ")  # e -> estudiantes
        estudiantes.append([e])

        examen1()
        examen2()
        tarea1()
        tarea2()
        proyecto()
        print("-" * 30)
        recorrido()
        x += 1
        pf += 1

# Función para agregar la nota del examen 1
def examen1():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en el examen 1: "))
    estudiantes[pf].insert(1, c1)

# Función para agregar la nota del examen 2
def examen2():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en el examen 2: "))
    estudiantes[pf].insert(2, c1)

# Función para agregar la nota de la tarea 1
def tarea1():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en la tarea 1: "))
    estudiantes[pf].insert(3, c1)

# Función para agregar la nota de la tarea 2
def tarea2():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en la tarea 2: "))
    estudiantes[pf].insert(4, c1)

# Función para agregar la nota del proyecto
def proyecto():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en el proyecto: "))
    estudiantes[pf].insert(5, c1)

# Función para calcular el promedio de cada estudiante
def recorrido():
    global p, pf
    for i in range(1, len(estudiantes)):
        suma = 0
        for j in range(1, len(estudiantes[i])):
            suma += estudiantes[i][j]
        promedioe.append(suma / 5)

# Inicialización de variables
promedioe = []

# Inicio del código
c = int(input("Ingrese la cantidad de estudiantes: "))  # c -> cantidad
x = 1
pf = 1
notas()

# Imprimir matriz
for i in estudiantes:
    print(i)
print("El promedio de cada estudiante es: ", promedioe)

# Encontrar el estudiante con el promedio más alto y más bajo
promediom = max(promedioe)
promediomin = min(promedioe)
indicem = promedioe.index(promediom)
indicemin = promedioe.index(promediomin)

promedio_e_max = estudiantes[indicem + 1][0]
promedio_e_min = estudiantes[indicemin + 1][0]

print(f"El estudiante con el promedio más alto es: {promedio_e_max} con un promedio de {promediom}")
print(f"El estudiante con el promedio más bajo es: {promedio_e_min} con un promedio de {promediomin}")


#version 11