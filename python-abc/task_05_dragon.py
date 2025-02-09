#!/usr/bin/env python3

"""
Module: Dragon Mixins

This module demonstrates the use of mixins to compose behaviors without
creating deep inheritance hierarchies. The Dragon class inherits from both
SwimMixin and FlyMixin, gaining the ability to swim and fly.

Classes:
    SwimMixin: Provides swimming capability.
    FlyMixin: Provides flying capability.
    Dragon: Inherits from both mixins and can also roar.

Usage Example:
    draco = Dragon()
    draco.swim()  # Outputs: The creature swims!
    draco.fly()   # Outputs: The creature flies!
    draco.roar()  # Outputs: The dragon roars!
"""


class SwimMixin:
    """Mixin class that provides swimming capability."""
    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability."""
    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim, fly, and roar."""
    def roar(self):
        """Prints roaring behavior."""
        print("The dragon roars!")


# Test the Implementation
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
