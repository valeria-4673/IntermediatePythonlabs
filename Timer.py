def format ( hours, mins, secs):
    lista = [hours, mins, secs]
    lista_2= []
    for element in lista:
        if element < 10:
            lista_2.append('0'+ str(element))
        else:
             lista_2.append(str(element))
             
    final = ':'.join(lista_2)
    return final

class Timer:
    def __init__(self, hour, minutes, seconds ):
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return format(self.__hour, self.__minutes, self.__seconds)
    
    def next_second(self):
        control = self.__seconds + 1
        if control >= 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes >= 60:
                self.__minutes = 0
                self.__hour += 1
                if self.__hour >= 24:
                    self.__hour = 0
                    
        if control < 60:
            self.__seconds = control
            
        return self.__str__()
    
    def prev_second(self):
        control = self.__seconds - 1
        
        if control < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hour -= 1                
                if self.__hour < 0:
                    self.__hour = 23
                    
        if control > 0:
            self.__seconds = control
            
        return self.__str__()
    
timer = Timer(21, 37, 44)
print(timer)
print(timer.next_second())
print(timer.prev_second())
