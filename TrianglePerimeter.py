
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
        
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y
    
    def distance_from_point(self, point):
        coord_y = point.gety()
        en_y = abs(self.__y - coord_y)
        coord_x = point.getx()
        en_x = abs(self.__x - coord_x)
        return math.hypot(en_y, en_x)

class Triangle:
    def __init__(self, p0, p1, p2):
        self.puntos = [p0, p1, p2]
        self.__p0 = p0
        self.__p1 = p1
        self.__p2 = p2

    def perimeter(self):
        perim = 0
        
        for punto in self.puntos:
            for i in range (3):
                distancia = punto.distance_from_point(self.puntos[i])
                perim += distancia
        return perim/2
        
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
