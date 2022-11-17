from jordan_gauss import *


def equation_system_test(a_matrix, b_matrix):
    """Тест работы метода Жордана-Гауса на матрицах A и B"""
    x_matrix = matrix_transposition([Jordan_Gauss_method(a_matrix, b_matrix)])
    return matrix_mul(a_matrix, x_matrix) == b_matrix


def test_gauss_jordan_method_1():
    a_matrix = [
        [2, 3],
        [4, 3],
    ]
    b_matrix = [
        [2],
        [7],
    ]
    assert equation_system_test(a_matrix, b_matrix)


def test_gauss_jordan_method_2():
    a_matrix = [
        [-1, 2, 6],
        [3, -6, 0],
        [1, 0, 6],
    ]
    b_matrix = [
        [15],
        [-9],
        [5],
    ]
    assert equation_system_test(a_matrix, b_matrix)
