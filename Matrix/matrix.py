from vector.vector import *

EPS = 1E-5


def print_matrix(matrix: list):
    """Вывод матрицы"""
    assert is_matrix(matrix)
    for i in matrix:
        print_vector(i)


def is_matrix(matrix: list) -> bool:
    """Проверка на матрицу"""
    assert len(matrix) != 0 and len(matrix[0]) != 0
    len_of_matrix = len(matrix[0])
    for i in matrix:
        if len_of_matrix != len(i):
            return False
    return True


def is_same_size_matrix(matrix_1: list, matrix_2: list) -> bool:
    """Проверка на одинаковый размер матриц"""
    if is_matrix(matrix_1) and is_matrix(matrix_2) and len(matrix_1) == len(matrix_2):
        return True
    else:
        return False


def matrix_mul_on_scalar(matrix: list, scalar: int) -> list:
    """Умножение матрицы на скаляр"""
    assert is_matrix(matrix)
    result_matrix = matrix.copy()
    for i in range(len(result_matrix)):
        result_matrix[i] = mul_on_scalar(result_matrix[i], scalar)
    return result_matrix


def matrix_sum(matrix_1: list, matrix_2: list) -> list:
    """Сложение матриц"""
    assert is_same_size_matrix(matrix_1, matrix_2)
    result_matrix = []
    for i in range(len(matrix_1)):
        result_matrix.append(sum_of_scalar(matrix_1[i], matrix_2[i]))
    return result_matrix


def matrix_sub(matrix_1: list, matrix_2: list) -> list:
    """Вычитание матриц"""
    assert is_same_size_matrix(matrix_1, matrix_2)
    result_matrix = []
    for i in range(len(matrix_1)):
        result_matrix.append(sub_of_scalar(matrix_1[i], matrix_2[i]))
    return result_matrix


def matrix_transposition(matrix: list) -> list:
    """Транспонирование матриц"""
    assert is_matrix(matrix)
    result_matrix = []
    for i in range(len(matrix[0])):
        result_matrix.append([matrix[j][i] for j in range(len(matrix))])
    return result_matrix


def matrix_mul(matrix_1: list, matrix_2: list) -> list:
    """Умножение матриц"""
    assert is_matrix(matrix_1) and is_matrix(matrix_2)
    result_matrix = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result_matrix


def get_row(matrix: list, index: int) -> list:
    """Получить строку по индексу"""
    if is_matrix(matrix):
        if 0 <= index < len(matrix):
            return matrix[index]


def get_column(matrix: list, index: int) -> list:
    """Получить столбец по индексу"""
    if is_matrix(matrix):
        transposed_matrix = matrix_transposition(matrix)
        if 0 <= index < len(transposed_matrix):
            return get_row(transposed_matrix, index)

def del_column(matrix: list, index: int) -> list:
    """Удалить столбец по индексу"""
    if is_matrix(matrix):
        result_matrix = matrix.copy()
        for i in range(len(result_matrix)):
            result_matrix[i] = get_row(matrix, i)[:index]
        return result_matrix

def swap_rows(matrix: list, index_1: int, index_2: int) -> list:
    """Поменять строки местами с индексом index_1 на строку с индексом index_2"""
    if is_matrix(matrix):
        if 0 <= index_1 < len(matrix) and 0 <= index_2 < len(matrix):
            temp = matrix[index_1]
            matrix[index_1] = matrix[index_2]
            matrix[index_2] = temp
            return matrix


def mul_row_on_scalar(matrix: list, index: int, scalar: int) -> list:
    """Умножить строку на скаляр"""
    if is_matrix(matrix):
        if 0 <= index < len(matrix):
            matrix[index] = mul_on_scalar(matrix[index], scalar)
            return matrix


def sum_mul_rows(matrix: list, index_1: int, index_2: int, scalar: int) -> list:
    """Сложение строки матрицы с индексом index_1 на строку с индексом index_2, умноженную на скаляр"""
    if is_matrix(matrix):
        if 0 <= index_1 < len(matrix) and 0 <= index_2 < len(matrix):
            temp = mul_on_scalar(matrix[index_2].copy(), scalar)
            matrix[index_1] = sum_of_scalar(matrix[index_1], temp)
            return matrix


def sub_mul_rows(matrix: list, index_1: int, index_2: int, scalar: int) -> list:
    """Вычитание строки матрицы с индексом index_1 на строку с индексом index_2, умноженную на скаляр"""
    if is_matrix(matrix):
        if 0 <= index_1 < len(matrix) and 0 <= index_2 < len(matrix):
            temp = mul_on_scalar(matrix[index_2].copy(), scalar)
            matrix[index_1] = sub_of_scalar(matrix[index_1], temp)
            return matrix