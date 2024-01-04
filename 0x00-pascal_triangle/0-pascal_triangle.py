#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns pascal trianle
    """
    if n <= 0:
        return []

    result = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)

    return result
