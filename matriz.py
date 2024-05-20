matriz_Todo = [["Productos", "Productos 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5", "Producto 6",],
               ["Lunes", 1, 2, 3, 4, 5, 6,], 
               ["Martes", 0, 0, 0, 0, 0, 0,], 
               ["Miercoles", 0, 0, 0, 0, 0, 0,], 
               ["Jueves", 0, 0, 0, 0, 0, 0,], 
               ["Viernes", 0, 0, 0, 0, 0, 0,], 
               ["Sabado", 0, 0, 0, 0, 0, 0,], 
               ]

for i in range(len(matriz_Todo)):
    if matriz_Todo[i][0] == "Lunes":
        for j in range (1, len(matriz_Todo[1])):
            print("hola")