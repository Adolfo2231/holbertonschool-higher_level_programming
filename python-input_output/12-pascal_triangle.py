#!/usr/bin/python3

"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.
    Args:
        n (int): Number of rows in Pascal's triangle.
    Returns:
        list of lists: Pascal's triangle representation.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
