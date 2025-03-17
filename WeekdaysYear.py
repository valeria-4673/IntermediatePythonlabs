import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self, year, weekday):
        super().__init__()
        self.year = year
        self.weekday = weekday
        
    def count_weekday_in_year(self):
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        todos_meses = []
        for month in months:
            print('Para mes{}: {}'.format(month, self.monthdays2calendar(self.year, month)))
            mes = self.monthdays2calendar(self.year, month)
            todos_meses.append(mes)
            
        counter = 0
        for mes in  todos_meses:
            # print('El mes es: ', mes)
            for sem in mes:
                # print('la sem es: ', sem)
                for dia in sem:
                    # print('El dia es: ',dia)
                    if dia[1] == self.weekday:
                        if dia [0] != 0:
                            counter += 1
        print(counter)
                    

obj = MyCalendar(2019,0)
obj.count_weekday_in_year()
