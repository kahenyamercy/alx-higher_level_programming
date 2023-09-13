#!/usr/bin/python3
"""Define the pascal's triangl"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to row 'n'.

    Args:
    n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    list of lists: A list of lists representing Pascal's triangle.

    Returns an empty list if n <= 0.

    Example:
    >>> result = pascal_triangle(5)
    >>> for row in result:
    ...     print(row)
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # Initialize the first element of each row to 1
        if triangle:  # If there are previous rows
            prev_row = triangle[-1]  # Get the previous row
            for j in range(len(prev_row) - 1):
                # Calculate new element by adding two from previous row
                new_element = prev_row[j] + prev_row[j + 1]
                row.append(new_element)
            row.append(1)  # Add the last element, which is always 1
        triangle.append(row)

    return triangle
