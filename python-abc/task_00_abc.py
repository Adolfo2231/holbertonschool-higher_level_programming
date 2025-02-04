#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase abstracta que define la estructura base para los animales.
    Obliga a las subclases a implementar el método `sound()`.
    """
    @abstractmethod
    def sound(self):
        """Método abstracto que cada subclase debe implementar."""
        pass  # No tiene implementación aquí, las subclases deben definirlo


# Creando la subclase `Dog` que hereda de `Animal`
class Dog(Animal):
    """
    Clase que representa un perro. Implementa el método `sound()`.
    """
    def sound(self):
        return "Bark"


# Creando la subclase `Cat` que hereda de `Animal`
class Cat(Animal):
    """
    Clase que representa un gato. Implementa el método `sound()`.
    """
    def sound(self):
        return "Meow"
