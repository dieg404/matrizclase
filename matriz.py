supermercado = [
               ["Productos", "  Lunes  ", " Martes  ", "Miercoles", " Jueves  ", " Viernes ", " Sabado  "],
               ["    |    ", "    |    ", "    |    ", "    |    ", "    |    ", "    |    ", "    |    "], 
               ["    v    ", "    v    ", "    v    ", "    v    ", "    v    ", "    v    ", "    v    "], 
               ]

#Funcion de bulce para agregar los productos que se vendio
def productos():
    global x, pf, p
    while x <= c:
        p = input(f"Ingrese el producto número {x} que vendió: ") #p -> productos
        supermercado.append([p])

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

# Función para agregar cuantos productos se vendieron por día, Lunes.
def lunes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Lunes: "))
    if c1 < 10:
        supermercado[pf].insert(1, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(1, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(1, f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Martes.
def martes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Martes: "))
    if c1 < 10:
        supermercado[pf].insert(2, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(2, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(2, f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Miércoles.
def miercoles():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Miércoles: "))
    if c1 < 10:
        supermercado[pf].insert(3, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(3, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(3, f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Jueves.
def jueves():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Jueves: "))
    if c1 < 10:
        supermercado[pf].insert(4, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(4, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(4, f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Viernes.
def viernes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Viernes: "))
    if c1 < 10:
        supermercado[pf].insert(5, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(5, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(5, f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Sábado.
def sabado():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Sábado: "))
    if c1 < 10:
        supermercado[pf].insert(6, f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].insert(6, f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].insert(6, f"    {c1}  ")
    else:
        print("Esto no debe salir.")


contador = 0
listap = []

def recorrdio():
    for i in range (len(supermercado)):
        if supermercado[i][0] == p:
            for j in i:
                listap.append(j)




#Inicio codigo.
c = int(input("Ingrese la cantidad de productos que vendio: ")) #c -> cantidad
x = 1
pf = 3 
productos()

print ("Su lista de numeros es ", listap)
 

#Imprimir matriz
for i in supermercado:
    print(i)

#version 3