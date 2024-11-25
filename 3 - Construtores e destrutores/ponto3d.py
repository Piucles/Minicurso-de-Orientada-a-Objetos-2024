from ponto import *

class Ponto3D(Ponto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, valor):
        self.__z = valor

    def __eq__(self, p):
        if (self.x == p.x and self.y == p.y and self.z == p.z):
            return True
        return False
    
    def __add__(self, p):
        result = Ponto3D(0,0,0)
        result.x = self.x + p.x
        result.y = self.y + p.y
        result.z = self.z + p.z
        return result
    
    def distancia(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        dz = p.z - self.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    
    def __str__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z)
    