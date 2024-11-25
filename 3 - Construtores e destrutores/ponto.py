import math

class Ponto:
    def __init__(self, x,y):
        self.__x = x
        self.__y = y
    
    def __del__(self):
        print("objeto destruido")

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, valor):
        self.__x = valor

    @property
    def y(self):
        return self.__y
    @x.setter
    def y(self, valor):
        self.__y = valor

    def __eq__(self, p):
        if (self.x == p.x and self.y == p.y):
            return True
        return False

    def __add__(self, p):
        result = Ponto(0,0)
        result.x = self.x + p.x
        result.y = self.y + p.y
        return result
    
    def distancia(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        return math.sqrt(dx*dx + dy*dy)

    def __str__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y)
    