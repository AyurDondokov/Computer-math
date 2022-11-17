from Matrix.matrix import *


def leading_element_index(matrix, index):
    """Ведущий элемент строки index в матрице matrix"""
    i = 0
    while matrix[index][i] == 0:
        i += 1
    return i


def forward_stroke(matrix):
    """Прямой ход"""
    n = len(matrix)
    for i in range(n):
        idx_swap_row = leading_element_index(matrix, i)

        if idx_swap_row != i:
            swap_rows(matrix, i, idx_swap_row)

        if matrix[i][i] != 1:
            mul_row_on_scalar(matrix, i, 1 / matrix[i][i])

        for j in range(i + 1, n):
            sub_mul_rows(matrix, j, i, matrix[j][i])


def backward_stroke(matrix):
    """Обратный ход"""
    n = len(matrix)
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if matrix[j][i] != 0:
                sub_mul_rows(matrix, j, i, matrix[j][i])


def Jordan_Gauss_method(a_matrix, b_matrix):
    """Метод Жордана-Гауса"""
    assert is_matrix(a_matrix) and is_matrix(b_matrix) and len(b_matrix[0]) == 1
    matrix = a_matrix.copy()
    for i in range(len(matrix)):
        matrix[i].append(b_matrix[i][0])
    print("\nРасширенная матрица A|B:")
    print_matrix(matrix)

    forward_stroke(matrix)
    print("\nПрямой ход:")
    print_matrix(matrix)

    backward_stroke(matrix)
    print("\nОбратный ход:")
    print_matrix(matrix)

    print("\nКорни уравнения:")
    last_column_index = len(matrix[0])-1
    roots = get_column(matrix, last_column_index)
    print(roots)

    return roots
