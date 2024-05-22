supermercado = [["Productos", ],
               ["Lunes", ], 
               ["Martes", ], 
               ["Miercoles", ], 
               ["Jueves", ], 
               ["Viernes", ], 
               ["Sabado", ], 
               ]




#Funcion de bulce para agregar los productos que se vendio
def productos():
    global x
    while x <= c:
        p = input(f"Ingrese el producto número {x} que vendió: ") #p -> productos
        supermercado[0].insert(1, p)
        lunes()
        martes()
        miercoles()
        jueves()
        viernes()
        sabado()
        print("-" * 30)
        

        x += 1


def lunes():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Lunes: "))
    supermercado[1].insert(1, c1)

def martes():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Martes: "))
    supermercado[2].insert(1, c1)

def miercoles():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Miercoles: "))
    supermercado[3].insert(1, c1)

def jueves():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Jueves: "))
    supermercado[4].insert(1, c1)

def viernes():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Viernes: "))
    supermercado[5].insert(1, c1)

def sabado():
    c1 = int(input(f"Ingrese la cantidad que vendio del producto el dia Sabado: "))
    supermercado[6].insert(1, c1)
    
    


c = int(input("Ingrese la cantidad de productos que vendio: ")) #c -> cantidad
x = 1
productos()


for i in supermercado:
    print(i)