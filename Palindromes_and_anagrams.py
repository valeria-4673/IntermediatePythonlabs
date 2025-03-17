# LAB Anagrams

import sys

word_1 = input("Escriba: ")
word_2 = input("Escriba: ")

# procesar strings

def procesar(stringi):
    s1 = stringi.replace(' ', '')
    s2 = s1.upper()
    return s2

stringi_1 = procesar(word_1)
print(stringi_1)
stringi_2 = procesar(word_2)
print(stringi_2)

# hallar iguales, mayor, menor
    
if len (stringi_1) == len (stringi_2):
    
    lista_1 = list(stringi_1)
    lista_2 = list(stringi_2)
    
    lista_1_sorted = lista_1.sort()
    lista_2_sorted = lista_2.sort()

    if lista_1_sorted == lista_2_sorted:
        print("Anagramas")
        sys.exit()

if len (stringi_1) >  len (stringi_2):
    mayor = stringi_1
    print('mayor', mayor)
    menor = stringi_2
    print('menor', menor)
elif len (stringi_1) <  len (stringi_2):
    mayor = stringi_2
    print('mayor', mayor)
    menor = stringi_1
    print('menor', menor)

# evaluando 
for ch in menor:
    comprobando = mayor.find(ch)
    if comprobando == -1:
        print('Not anagrams')
        break
else:
    print('Anagrams')
  
  #LAB Palindromes

word = input("Escriba: ")

no_spaces = word.replace(' ', '')
print(no_spaces)
mayus = no_spaces.upper()

l_mayus = list(mayus)
print(l_mayus)

l_mayus_2 = l_mayus[::-1]
print(l_mayus)

if l_mayus == l_mayus_2:
    print("Palindromes")
else:
    print("Not palindromes")
