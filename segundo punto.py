estudiantes = [
              ["Estudiantes"], ["Examen 1"], ["Examen 2"], ["Tarea 1"], ["Tarea 2"], ["Proyecto"]
              ] 


#Funcion de bucle para agregar los estudiantes y sus notas
def notas():
    global x, pf, e
    while x <= c:
        e = input(f"Ingrese el nombre del estudiante número {x}: ") #e -> estudiantes
        estudiantes.append([e])

         






        lunes()
        martes()
        miercoles()
        jueves()
        viernes()
        sabado()
        print("-" * 30)
        recorrdio()
        x += 1
        pf += 1
        

# Función para agregar la nota del examen 1
def examen1():
    c1 = int(input(f"Ingrese la nota que obtuvo el estudiante en el examen 1: "))
    estudiantes[pf].insert(1, c1) 

# Función para agregar cuantos productos se vendieron por día, Martes.
def martes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Martes: "))
    supermercado[pf].insert(2, c1)

# Función para agregar cuantos productos se vendieron por día, Miércoles.
def miercoles():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Miércoles: "))
    supermercado[pf].insert(3, c1)

# Función para agregar cuantos productos se vendieron por día, Jueves.
def jueves():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Jueves: "))
    supermercado[pf].insert(4, c1)

# Función para agregar cuantos productos se vendieron por día, Viernes.
def viernes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Viernes: "))
    supermercado[pf].insert(5, c1)

# Función para agregar cuantos productos se vendieron por día, Sábado.
def sabado():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Sábado: "))
    supermercado[pf].insert(6, c1)


def recorrdio():
    global p, pf
    for i in range(1, len(supermercado)):
        sum = 0
        for j in range (1, len(supermercado [i])):
            sum += supermercado[i][j]
    valorp.append(sum)

def recorridod():
    global p, pf, diariop
    for i in range(1, len(supermercado)):
        for j in range(1, len(supermercado[i])):
            diariop[j-1] += supermercado[i][j]
    
    
diariop =[0,0,0,0,0,0]  
        
valorp = []

#Inicio codigo.
c = int(input("Ingrese la cantidad de productos que vendio: ")) #c -> cantidad
x = 1
pf = 1 
productos()
recorridod()

#Imprimir matriz
for i in supermercado:
    print(i)
print("La venta total de cada producto durante la semana en su orden es: ", valorp)

print("La venta total de los prodcutos vendidos es:", sum(valorp))

print("La venta diaria de los productos en la semana es", diariop)

#version 9