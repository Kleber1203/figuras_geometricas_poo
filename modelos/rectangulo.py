from modelos.figura import Figura

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base      # encapsulación
        self.__altura = altura  # encapsulación

    def calcular_area(self):
        return self.__base * self.__altura
