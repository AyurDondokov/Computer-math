from .vector import *


def test_sum_of_scalar():
    res = sum_of_scalar((1, 0), (0, 1))
    assert are_vectors_almost_equals(res, (1, 1))


def test_sub_of_scalar():
    res = sub_of_scalar((1, 1), (1, 1))
    assert are_vectors_almost_equals(res, (0, 0))


def test_mul_on_scalar():
    res = mul_on_scalar((1, 1), 2)
    assert are_vectors_almost_equals(res, (2, 2))


def test_dif_on_scalar():
    res = dif_on_scalar((2, 2), 2)
    assert are_vectors_almost_equals(res, (1, 1))


def test_scalar_mul():
    res = scalar_mul((1, 2, -5), (4, 8, 1))
    assert are_scalars_almost_equals(res, 15)


def test_is_co_lineal():
    res = is_colineal((0, 2), (0, 4))
    assert res


def test_angle_bet_vectors():
    res = angle_bet_vectors((0, 2), (2, 0))
    assert are_scalars_almost_equals(res, 90)


def test_is_co_direction():
    res = is_co_direction((0, 2), (0, 4))
    assert res


def test_is_counter_direction():
    res = is_counter_direction((0, -2), (0, 4))
    assert res


def test_length():
    res = length((0, 2))
    assert are_scalars_almost_equals(res, 2)


def test_is_equals():
    res = is_equals((6, 4), (6, 4))
    assert res


def test_cos():
    res = cos((0, 2), (2, 0))
    assert are_scalars_almost_equals(res, 0)


def test_is_orthogonal():
    res = is_orthogonal((0, 2), (2, 0))
    assert res


def test_scalar_projection():
    res = scalar_projection((1, 2), (3, 4))
    assert are_scalars_almost_equals(res, 2.2)


def test_vector_projection():
    res = vector_projection((4, 5), (6, 0))
    assert are_vectors_almost_equals(res, (4, 0))
