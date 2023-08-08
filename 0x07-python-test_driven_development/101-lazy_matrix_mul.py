#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""
Defines a function that multiplies two matrices using the NumPy module.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        ValueError: If m_a or m_b is not valid for matrix multiplication.
    """

    return np.dot(m_a, m_b)
