from abc import ABC, abstractmethod
import math

# OCP: Interfaz común abierta a extensiones pero cerrada a modificaciones
class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

# SRP: Cada clase tiene una única responsabilidad (calcular el área de su propia figura)
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

# ¿Cómo añadimos una nueva figura sin modificar el código anterior?
# Simplemente creamos una nueva clase que herede de FiguraGeometrica:
class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

# Ejemplo de uso polimórfico:
if __name__ == "__main__":
    figuras = [
        Cuadrado(4),
        Circulo(3),
        Triangulo(5, 2)
    ]

    for figura in figuras:
        print(f"Área calculada: {figura.calcular_area():.2f}")