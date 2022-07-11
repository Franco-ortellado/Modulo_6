import math

def area_triangulo(base,altura):
    
    area = (base*altura)/2
    return area

def area_circulo(radio):
    
    area = math.pi*(radio)**2
    return area


print("Area del Triangulo:",area_triangulo(3,4))

print("Area del Circulo:",area_circulo(3))