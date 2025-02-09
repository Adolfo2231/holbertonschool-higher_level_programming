#!/usr/bin/env python3

"""
Module: FlyingFish

This module demonstrates multiple inheritance in Python by defining a
FlyingFish class that inherits from both Fish and Bird. The class overrides
methods from both parent classes to represent a flying fish's unique
abilities.

Classes:
    Fish: Represents a fish with swimming ability and water habitat.
    Bird: Represents a bird with flying ability and sky habitat.
    FlyingFish: Inherits from Fish and Bird, overriding methods to define
        behavior specific to a flying fish.

Usage Example:
    flying_fish = FlyingFish()
    flying_fish.swim()  # Prints: The flying fish is swimming!
    flying_fish.fly()   # Prints: The bird is flying
    flying_fish.habitat()  # Prints: The flying fish lives both in water
                           # and the sky!
    print(FlyingFish.mro())  # Prints method resolution order
"""


class Fish:
    """
    Represents a fish that can swim and lives in water.
    """
    def swim(self):
        """Prints swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat information."""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird that can fly and lives in the sky.
    """
    def fly(self):
        """Prints flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat information."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish that can swim and fly.
    """
    def swim(self):
        """Overrides swim method to represent flying fish swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides fly method to represent flying fish flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides habitat method to describe its dual habitat."""
        print("The flying fish lives both in water and the sky!")


# Test the Implementation
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())  # Verify method resolution order (MRO)
