Sudoku verificando filas

sudoku = input("Escriba: ") # escribir las 9 filas, al final sin espacio
filas = sudoku.split(' ')
print(filas)

elementxelement = []

for stringi in filas:
    provisional = []
    for ch in stringi:
        provisional.append(ch)
    elementxelement.append(provisional)
    
print(elementxelement)

# verificando filas

for fila in elementxelement:
    fila_ordenada = sorted (fila)
    print(fila_ordenada)
    if fila_ordenada != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Filas no validas')
        break
else:
    print('filas válidas')

# verificando columnas 3x3

sudoku = input("Escriba: ") # escribir al final sin espacio
filas = sudoku.split(' ')
print(filas)

# hacer filas
elementxelement = []

for stringi in filas:
    provisional = []
    for ch in stringi:
        provisional.append(ch)
    elementxelement.append(provisional)
    
print(elementxelement)

# hacer las columnas
columnas = []

for j in range(3):
    columna = []
    for i in range (3):
        val= elementxelement[i][j]
        columna.append(val)
    columnas.append(columna)

print(columnas)

# Otro programa verificar las columnas

for substringi in columnas:
    ordered_substringi = sorted(substringi)
    print(ordered_substringi)
    if ordered_substringi != ['1', '2', '3']:
        print('Columna invalida')
        break
else:
    print('Las columnas son válidas') # 132 221 313
