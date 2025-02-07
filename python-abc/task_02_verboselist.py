#!/usr/bin/env python3

from abc import ABC, abstractmethod


"""
Este módulo define la clase VerboseList, que extiende la funcionalidad de la
clase `list` en Python para imprimir mensajes cuando se agregan o eliminan
elementos.
"""


class VerboseList(list):
    """
    Clase que extiende `list` para notificar cuando se realizan modificaciones.
    """

    def append(self, item):
        """
        Agrega un elemento a la lista y muestra un mensaje.

        :param item: Elemento a agregar.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Agrega múltiples elementos a la lista y muestra un mensaje.

        :param iterable: Colección de elementos a agregar.
        """
        count = len(list(iterable))
        super().extend(iterable)
        if count > 0:
            print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Elimina un elemento de la lista y muestra un mensaje.

        :param item: Elemento a eliminar.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Elimina un elemento de la lista por índice y muestra un mensaje.

        :param index: Índice del elemento a eliminar (por defecto, el último).
        :return: Elemento eliminado o None si la lista está vacía.
        """
        if self:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("Cannot pop from an empty list.")
            return None


# ✅ Prueba del código con VerboseList
if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])

    vl.append(4)  # "Added [4] to the list."
    vl.extend([5, 6])  # "Extended the list with [2] items."
    vl.remove(2)  # "Removed [2] from the list."
    vl.pop()  # "Popped [6] from the list."
    vl.pop(0)  # "Popped [1] from the list."
