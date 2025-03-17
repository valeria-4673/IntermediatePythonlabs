class WeekDayError(Exception):
    pass

class Weeker:
    accept = ['Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    accept_2 = ['Sun', 'Sat','Fri', 'Thu', 'Wed', 'Tue', 'Mon']
    
    def __init__(self, day):
        self.__day = day
        if day not in self.accept:
            raise WeekDayError

    def __str__(self):
        return self.__day

    def add_days(self, n):
        x = n % 7
        pos_nuev =(self.accept.index(self.__day) + x) % 7
        self.__day = self.accept [pos_nuev]
        return self.accept [pos_nuev]
        
    def subtract_days(self, n):
        posi_dado = self.accept.index(self.__day)
        buscar_reversa = (n + (6 -  posi_dado)) % 7
        self.__day = self.accept_2[buscar_reversa]
        return self.accept_2[buscar_reversa]
try:
    weekday = Weeker('Mon')
    print(weekday)
    print(weekday.add_days(15))
    print(weekday.subtract_days(23))
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
