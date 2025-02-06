#!/usr/bin/env python3

from abc import ABC, abstractmethod


"""
Este módulo define una jerarquía de clases para representar figuras geométricas
utilizando clases abstractas y Duck Typing.
"""


class Shape(ABC):
    """
    Clase abstracta que sirve como plantilla para cualquier figura geométrica.
    Define los métodos abstractos `area` y `perimeter` que deben ser
    implementados por las subclases.
    """
    @abstractmethod
    def area(self):
        """
        Método abstracto para calcular el área de la figura.
        Debe ser implementado en las subclases.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Método abstracto para calcular el perímetro de la figura.
        Debe ser implementado en las subclases.
        """
        pass


class Circle(Shape):
    """
    Representa un círculo con un radio específico.
    Implementa los métodos `area` y `perimeter`.
    """

    def __init__(self, radius):
        """
        Inicializa un círculo con un radio dado.
        param radius: Radio del círculo.
        """
        self.radius = radius

    def area(self):
        """
        Calcula el área del círculo usando la fórmula A = π * r².

        :return: Área del círculo.
        """
        return 3.14159265359 * (self.radius ** 2)

    def perimeter(self):
        """
        Calcula el perímetro (circunferencia)
        del círculo usando la fórmula P = 2 * π * r.

        :return: Perímetro del círculo.
        """
        return 2 * 3.14159265359 * self.radius


class Rectangle(Shape):
    """
    Representa un rectángulo con ancho y alto específicos.
    Implementa los métodos `area` y `perimeter`.
    """

    def __init__(self, width, height):
        """
        Inicializa un rectángulo con ancho y alto dados.

        :param width: Ancho del rectángulo.
        :param height: Altura del rectángulo.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcula el área del rectángulo usando
        la fórmula A = ancho * altura.

        :return: Área del rectángulo.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcula el perímetro del rectángulo usando
        la fórmula P = 2 * (ancho + altura).

        :return: Perímetro del rectángulo.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Imprime el área y el perímetro de un objeto que
    implementelos métodos `area` y `perimeter`.
    Utiliza Duck Typing, por lo que cualquier objeto
    que tenga estos métodos puede ser pasado.

    :param shape: Objeto que implementa los métodos `area()` y `perimeter()`.
    """
    print(f"Área: {shape.area()}")
    print(f"Perímetro: {shape.perimeter()}")
