from matrix_catalog.matrix import *


def leading_element_index(matrix: list, index: int) -> int:
    """Ведущий элемент строки index в матрице matrix_catalog"""
    i = 0
    while matrix[index][i] == 0:
        i += 1
    return i


def forward_stroke(matrix: list) -> list:
    """Прямой ход"""
    result_matrix = matrix.copy()
    n = len(result_matrix)
    for i in range(n):
        idx_swap_row = leading_element_index(result_matrix, i)

        if idx_swap_row != i:
            swap_rows(result_matrix, i, idx_swap_row)

        if result_matrix[i][i] != 1:
            mul_row_on_scalar(result_matrix, i, 1 / result_matrix[i][i])

        for j in range(i + 1, n):
            sub_mul_rows(result_matrix, j, i, result_matrix[j][i])
    return result_matrix


def backward_stroke(matrix: list) -> list:
    """Обратный ход"""
    result_matrix = matrix.copy()
    n = len(result_matrix)
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if result_matrix[j][i] != 0:
                sub_mul_rows(result_matrix, j, i, result_matrix[j][i])
    return result_matrix


def get_expanded_matrix(a_matrix: list, b_matrix: list) -> list:
    result_matrix = a_matrix.copy()
    for i in range(len(result_matrix)):
        result_matrix[i].append(matrix_transposition([b_matrix])[i][0])
    return result_matrix


def jordan_gauss_method(a_matrix: list, b_matrix: list,
                        print_process: bool = False) -> list:
    """Метод Жордана-Гауса"""
    assert is_matrix(a_matrix) and len(b_matrix) == len(a_matrix)
    matrix = get_expanded_matrix(a_matrix, b_matrix)

    if print_process:
        print("\nРасширенная матрица A|B:")
        print_matrix(matrix)

    matrix = forward_stroke(matrix)
    if print_process:
        print("\nПрямой ход:")
        print_matrix(matrix)

    matrix = backward_stroke(matrix)
    if print_process:
        print("\nОбратный ход:")
        print_matrix(matrix)

    last_column_index = len(matrix[0])-1
    roots = get_column(matrix, last_column_index)
    if print_process:
        print("\nКорни уравнения:")
        print(roots)

    return roots
