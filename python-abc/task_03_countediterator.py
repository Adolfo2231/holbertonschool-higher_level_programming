#!/usr/bin/env python3

"""
Module: CountedIterator

This module defines `CountedIterator`,which extends Python's built-in iterator.
It tracks the number of items iterated over.

Features:
- Overrides `__next__` to count accessed elements.
- Provides `get_count()` to retrieve the count.
- Raises `StopIteration` when no more items remain.
"""


class CountedIterator:
    """
    Iterator that tracks the number of iterated items.
    """

    def __init__(self, iterable):
        """
        Initialize with an iterable.

        :param iterable: Iterable object.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return self as an iterator.
        """
        return self

    def __next__(self):
        """
        Fetch next item and increment the counter.

        :return: Next item.
        :raises StopIteration: If no items remain.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Return count of iterated items.
        """
        return self.count


# Example Usage:
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} iterated.")
    except StopIteration:
        print("No more items.")
