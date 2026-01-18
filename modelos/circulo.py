from modelos.figura import Figura
import math

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio  # encapsulación

    def calcular_area(self):
        return math.pi * self.__radio ** 2
