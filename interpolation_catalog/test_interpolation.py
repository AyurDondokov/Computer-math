import interpolation_catalog.interpolation as ipol
import interpolation_catalog.draw_interpolation as draw_ipol
import vector_catalog.vector as vec


def test_do_interpolation_1():
    assert ipol.do_interpolation([[2, 5], [6, 9]], [1, 4]) == [4.0, 7.0]


def test_piecewise_linear_interpolation():
    assert vec.are_vectors_almost_equals(ipol.piecewise_linear_interpolation(
        [[1, 2], [3, 4], [3.5, 3], [6, 7]], [-1.5, 3, 2, 5, 9]), [-0.5, 4, 3, 5.4, 11.8])


def test_lagrange_polynomial():
    assert vec.are_scalars_almost_equals(ipol.lagrange_polynomial([[1, 2],
                                   [3, 4],
                                   [3.5, 3],
                                   [6, 7]], 2), 4.92)

