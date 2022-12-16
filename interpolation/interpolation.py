from gauss_jordan.jordan_gauss import *


def line_equation(data_xy,
                  print_process: bool = False):
    assert is_matrix(data_xy) and len(data_xy) == 2
    a_matrix = []
    b_matrix = []
    for i in range(len(data_xy)):
        a_matrix.append([data_xy[i][0], 1])
        b_matrix.append(data_xy[i][1])
    if print_process:
        print("\nМатрица A:")
        print_matrix(a_matrix)
        print("\nМатрица В:")
        print(b_matrix)

    roots = jordan_gauss_method(a_matrix, b_matrix)
    if print_process:
        print(f"\nЛинейное уравнение для двух точек: {roots[0]}x + {roots[1]} = y")

    return roots


def piecewise_linear_interpolation(data_xy,
                                   print_process: bool = False):
    result_xy = []
    for i in range(len(data_xy)-1):
        d_xy = [data_xy[i], data_xy[i+1]]
        result_xy.append(line_equation(d_xy, print_process))
    print(result_xy)


def lagrange_polynomial(data_xy):




xy = [
    [1, 2],
    [3, 4],
    [3.5, 3],
    [6, 7]
]
piecewise_linear_interpolation(xy, True)
