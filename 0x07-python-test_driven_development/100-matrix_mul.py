#!/usr/bin/python3
"""matmul function"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list
            of lists, or if m_a contains elements other than integers or floats
            or if m_b contains elements other than integers or floats, or if
            each row of m_a is not of the same size, or if each row of m_b is
            not of the same size.
        ValueError: If m_a or m_b is empty or if m_a & m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(li, list) for li in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(li, list) for li in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for li in m_a for num in li):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for li in m_b for num in li):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(li) for li in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(li) for li in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
