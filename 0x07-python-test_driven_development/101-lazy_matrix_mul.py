#!/usr/bin/python3
"""
Defines lazy_matrix function multiplies 2 matrices by using the module NumPy
"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    return numpy.matmul(m_a, m_b)