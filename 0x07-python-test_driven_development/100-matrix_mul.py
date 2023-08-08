#!/usr/bin/python3
# 100-matrix_mul.py
#!/usr/bin/python3
"""
Defines a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty or contains non-int/float elements.
        TypeError: If each row of m_a or m_b is not of the same size.
        ValueError: If m_a and m_b cannot be multiplied.
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise ValueError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise ValueError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    cols_a = len(m_a[0])
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    cols_b = len(m_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
