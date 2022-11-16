
from Vector.Vector import *

EPS = 1E-5


def print_matrix(m):
    """Вывод матрицы"""
    assert is_matrix(m)
    for i in m:
        print_vector(i)


def is_matrix(m):
    """Проверка на матрицу"""
    assert len(m) != 0 and len(m[0]) != 0
    len_of_matrix = len(m[0])
    for i in m:
        if len_of_matrix != len(i):
            return False
    return True


def is_same_size_matrix(m1, m2):
    """Проверка на одинаковый размер матриц"""
    if is_matrix(m1) and is_matrix(m2) and len(m1) == len(m2):
        return True
    else:
        return False


def matrix_mul_on_scalar(m, s):
    """Умножение матрицы на скаляр"""
    assert is_matrix(m)
    for i in range(len(m)):
        m[i] = mul_on_scalar(m[i], s)
    return m


def matrix_sum(m1, m2):
    """Сложение матриц"""
    assert is_same_size_matrix(m1, m2)
    new_m = []
    for i in range(len(m1)):
        new_m.append(sum_of_scalar(m1[i], m2[i]))
    return new_m


def matrix_sub(m1, m2):
    """Вычитание матриц"""
    assert is_same_size_matrix(m1, m2)
    new_m = []
    for i in range(len(m1)):
        new_m.append(sub_of_scalar(m1[i], m2[i]))
    return new_m


def matrix_transposition(m):
    """Транспонирование матриц"""
    assert is_matrix(m)
    new_m = []
    for i in range(len(m[0])):
        new_m.append([m[j][i] for j in range(len(m))])
    return new_m


def matrix_mul(m1, m2):
    """Умножение матриц"""
    assert is_matrix(m1) and is_matrix(m2)
    new_m = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                new_m[i][j] += m1[i][k] * m2[k][j]
    return new_m


def get_row(m, i):
    """Получить строку по индексу"""
    if is_matrix(m):
        if 0 <= i < len(m):
            return m[i]


def get_column(m, i):
    """Получить столбец по индексу"""
    if is_matrix(m):
        t_m = matrix_transposition(m)
        if 0 <= i < len(t_m):
            return get_row(t_m, i)


def swap_rows(m, i1, i2):
    """Поменять строки местами"""
    if is_matrix(m):
        if 0 <= i1 < len(m) and 0 <= i2 < len(m):
            temp = m[i1]
            m[i1] = m[i2]
            m[i2] = temp
            return m


def multiply_row_on_scalar(m, i, scalar):
    """Умножить строку на скаляр"""
    if is_matrix(m):
        if 0 <= i < len(m):
            m[i] = mul_on_scalar(m[i], scalar)
            return m


def sum_mul_rows(m, i_1, i_2, scalar):
    """Сложение строки матрицы с индексом i_1 на строку с индексом i_2, умноженную на скаляр"""
    if is_matrix(m):
        if 0 <= i_1 < len(m) and 0 <= i_2 < len(m):
            temp = mul_on_scalar(m[i_2].copy(), scalar)
            m[i_1] = sum_of_scalar(m[i_1], temp)
            return m


def sub_mul_rows(m, i_1, i_2, scalar):
    """Вычитание строки матрицы с индексом i_1 на строку с индексом i_2, умноженную на скаляр"""
    if is_matrix(m):
        if 0 <= i_1 < len(m) and 0 <= i_2 < len(m):
            temp = mul_on_scalar(m[i_2].copy(), scalar)
            m[i_1] = sub_of_scalar(m[i_1], temp)
            return m
