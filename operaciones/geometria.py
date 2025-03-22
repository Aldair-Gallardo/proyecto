import math

def area_circulo(Radio):  
    Area =  math.pi * pow(Radio, 2)
    return Area

def perimetro_circulo(Radio):
    Perimetro = 2 * math.pi * Radio
    return Perimetro

def area_rectangulo(Base, Altura):
    Area = Base * Altura
    return Area

def perimetro_rectangulo(Base, Altura):
    Perimetro = 2 * (Base + Altura)
    return Perimetro
