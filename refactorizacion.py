def calcular_area_cuadrado(lado: float) -> float:
    """Calcula y retorna el área de un cuadrado."""
    return lado ** 2

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula y retorna el área de un rectángulo."""
    return base * altura

def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula y retorna el área de un triángulo."""
    return (base * altura) / 2

# Ejemplo de uso:
if __name__ == "__main__":
    print("Área del cuadrado (lado 5):", calcular_area_cuadrado(5))
    print("Área del rectángulo (base 4, altura 10):", calcular_area_rectangulo(4, 10))
    print("Área del triángulo (base 6, altura 3):", calcular_area_triangulo(6, 3))