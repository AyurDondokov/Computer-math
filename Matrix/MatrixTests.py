from .Matrix import *


def test_matrix_mul_on_scalar():
    m = [
        [1],
        [3],
        [5]
    ]
    res = matrix_mul_on_scalar(m, 5)
    assert res == [[5], [15], [25]]


def test_matrix_sum():
    m1 = [
        [1],
        [3],
        [5]
    ]
    m2 = [
        [2],
        [2],
        [2]
    ]
    res = matrix_sum(m1, m2)
    assert res == [[3], [5], [7]]


def test_matrix_sub():
    m1 = [
        [2],
        [3],
        [5]
    ]
    m2 = [
        [1],
        [2],
        [2]
    ]
    res = matrix_sub(m1, m2)
    assert res == [[1], [1], [3]]


def test_matrix_transposition():
    m = [
        [1],
        [3],
        [5]
    ]
    res = matrix_transposition(m)
    assert res == [[1, 3, 5]]


def test_matrix_mul():
    m1 = [
        [2],
        [3],
        [5]
    ]
    m2 = [[2, 4, 5]]
    res = matrix_mul(m1, m2)
    assert res == [[4, 8, 10], [6, 12, 15], [10, 20, 25]]


def test_get_row():
    m = [
        [1],
        [3],
        [5]
    ]
    res = get_row(m, 2)
    assert res == [5]


def test_get_column():
    m = [
        [1, 4, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]
    res = get_column(m, 2)
    assert res == [0, 8, 10]


def test_swap_rows():
    m = [
        [1, 4, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]
    res = swap_rows(m, 0, 2)
    assert res == [
        [5, 8, 10],
        [3, 6, 8],
        [1, 4, 0]
    ]


def test_multiply_row_on_scalar():
    m = [
        [1, 4, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]
    res = multiply_row_on_scalar(m, 0, 2)
    assert res == [
        [2, 8, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]


def test_sum_mul_rows():
    m = [
        [1, 4, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]
    res = sum_mul_rows(m, 0, 2, 2)
    assert res == [
        [11, 20, 20],
        [3, 6, 8],
        [5, 8, 10]
    ]


def test_sub_mul_rows():
    m = [
        [1, 4, 0],
        [3, 6, 8],
        [5, 8, 10]
    ]
    res = sub_mul_rows(m, 0, 2, 2)
    assert res == [
        [-9, -12, -20],
        [3, 6, 8],
        [5, 8, 10]
    ]
