from inverse_matrix_search import inverse_matrix
import vector.vector as vector


def test_inverse_matrix_1():
    assert inverse_matrix.get_inverse_matrix(
        [[1, 2], [3, 4]]) == [[-2, 1], [1.5, -0.5]]


def test_inverse_matrix_2():
    assert inverse_matrix.get_inverse_matrix(
        [[1, 1, 0], [0, 1, 0], [0, 3, 3]]) == [[1, -1, 0], [0, 1, 0], [0.0, -1.0, 0.3333333333333333]]


def test_get_root_1():
    assert inverse_matrix.get_roots(
        [[1, 2], [3, 4]], [6, 8]) == [-4.0, 5.0]


def test_get_root_2():
    assert vector.are_vectors_almost_equals(inverse_matrix.get_roots(
        [[1, -2, 1], [2, -1, 1], [3, 2, 2]], [1, 2, -2]), [2, -1, -3], 1E-10) is True
