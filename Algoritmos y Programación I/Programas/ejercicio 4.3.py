print("Este programa calcula la identidad d euna matriz cuadrada de dimension electa por el usuario")
dim = int(input("Ingrese la dimension de la matriz cuadrada: "))
M = [] # Matriz
for i in range(dim):
    fila = []
    for j in range(dim):
        val = 1 if i==j else 0
        fila.append(val)
    M.append(fila)
 
print (M)
