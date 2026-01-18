from modelos.rectangulo import Rectangulo
from modelos.circulo import Circulo

def calcular_areas():
    figuras = []

    rectangulo = Rectangulo(5, 3)
    circulo = Circulo(4)

    figuras.append(rectangulo)
    figuras.append(circulo)

    for figura in figuras:
        print(f"Área calculada: {figura.calcular_area():.2f}")
