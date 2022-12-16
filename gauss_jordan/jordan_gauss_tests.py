from gauss_jordan import jordan_gauss


def equation_system_test(a_matrix, b_matrix):
    """Тест работы метода Жордана-Гауса на матрицах A и B"""
    x_matrix = jordan_gauss.matrix_transposition([jordan_gauss.jordan_gauss_method(a_matrix, b_matrix)])
    return jordan_gauss.matrix_mul(a_matrix, x_matrix) == jordan_gauss.matrix_transposition([b_matrix])


def test_gauss_jordan_method_1():
    a_matrix = [
        [2, 1],
        [6, 1]
    ]
    b_matrix = [
        5,
        9
    ]
    assert equation_system_test(a_matrix, b_matrix)


def test_gauss_jordan_method_2():
    a_matrix = [
        [-1, 2, 6],
        [3, -6, 0],
        [1, 0, 6],
    ]
    b_matrix = [15, -9, 5]
    assert equation_system_test(a_matrix, b_matrix)
