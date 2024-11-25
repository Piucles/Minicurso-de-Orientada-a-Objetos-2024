from ponto3d import *

p1 = Ponto3D(3,5,2)
p2 = Ponto3D(10,10,10)

p3 = p1 + p2

result = p1.distancia(p2)

if (p1 == p2):
    print("Pontos iguais")
else:
    print("A distância é: ", result)

print(p1)
print(p2)
print(p3)
