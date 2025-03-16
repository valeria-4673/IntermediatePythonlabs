numbers =[
[[' ', ' ', '*', '  '], [' ', ' ', '*', '  '], [' ', ' ', '*', '  '], [' ', ' ', '*', '  '], [' ', ' ', '*', '  ']], # 1
[['*', '*', '*', '  '], [' ', ' ', '*', '  '], ['*', '*', '*', '  '], ['*', ' ', ' ', '  '], ['*', '*', '*', '  ']], # 2  
[['*', '*', '*', '  '], [' ', ' ', '*', '  '], ['*', '*', '*', '  '], [' ', ' ', '*', '  '], ['*', '*', '*', '  ']]] # 3
 
quiere = input('Numero : ')
hacer = []

for num in quiere:
    buscar = int(num)
    combinacion = numbers[buscar-1]
    hacer.append(combinacion)    
print(hacer)

print(len(hacer)) 

for j in range (5):
    renglon = []
    for i in range (len(hacer)):
        renglon += hacer[i][j]
    print(''.join(renglon))
