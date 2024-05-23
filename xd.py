supermercado = [
    ["Productos", "  Lunes  ", " Martes  ", "Miercoles", " Jueves  ", " Viernes ", " Sabado  "],
    ["    |    ", "    |    ", "    |    ", "    |    ", "    |    ", "    |    ", "    |    "],
    ["    v    ", "    v    ", "    v    ", "    v    ", "    v    ", "    v    ", "    v    "],
    [], 
    [], 
    [], 
    [], 
    [],
    [], 
]

# Función de bucle para agregar los productos que se vendieron
def productos():
    global x, pf
    while x <= c:
        p = input(f"Ingrese el producto número {x} que vendió: ")  # p -> productos
        supermercado[pf].append(p)  # Se agrega el producto en la primera columna de la fila correspondiente

        lunes()
        martes()
        miercoles()
        jueves()
        viernes()
        sabado()
        print("-" * 30)
        x += 1
        pf += 1

# Función para agregar cuantos productos se vendieron por día, Lunes.
def lunes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Lunes: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Martes.
def martes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Martes: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Miércoles.
def miercoles():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Miércoles: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Jueves.
def jueves():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Jueves: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Viernes.
def viernes():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Viernes: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Función para agregar cuantos productos se vendieron por día, Sábado.
def sabado():
    c1 = int(input(f"Ingrese la cantidad que vendió del producto el día Sábado: "))
    if c1 < 10:
        supermercado[pf].append(f"    {c1}    ")
    elif c1 >= 10 and c1 < 100:
        supermercado[pf].append(f"    {c1}   ")
    elif c1 >= 100 and c1 < 1000:
        supermercado[pf].append(f"    {c1}  ")
    else:
        print("Esto no debe salir.")

# Inicio del código.
c = int(input("Ingrese la cantidad de productos que vendió: "))  # c -> cantidad
x = 1
pf = 3 
productos()

# Imprimir matriz
for i in supermercado:
    print(i)
