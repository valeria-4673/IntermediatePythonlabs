def mysplit(strng):
    if strng.isspace() or strng == '': 
        return []
        
    lista_1 = []
    lista_2 =[]
    
    for i in range (len(strng)):
        
        if strng [i] != ' ':
            lista_1.append(strng [i])
            
        if strng [i] == ' ' or i == len(strng) -1 :
            palabra = ''.join(lista_1)
            
            if palabra == '':
                continue
            
            lista_2.append(palabra)
            lista_1 = []
            
    return lista_2  
       
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
