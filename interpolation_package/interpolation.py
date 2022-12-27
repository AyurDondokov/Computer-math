from gauss_jordan_package.jordan_gauss import *


def line_equation_get_ab(data_xy,
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


def line_equation_get_y(x, ab):
    a, b = ab
    y = x * a + b
    return y


def do_interpolation(data_xy, x_array,
                     print_process: bool = False):
    if print_process:
        print("Поиск AB:")
    ab = line_equation_get_ab(data_xy, print_process)
    y_array = []
    for x in x_array:
        y_array.append(line_equation_get_y(x, ab))
    return y_array


def lagrange_polynomial(data_xy, x):
    x_array = get_column(data_xy, 0)
    y_array = get_column(data_xy, 1)
    n = len(x_array)
    result = 0

    for i in range(n):
        basis = 1
        for j in range(n):
            if i == j:
                continue
            basis *= (x - x_array[j]) / (x_array[i] - x_array[j])
        result += y_array[i] * basis
    return result


def get_diapason(x, x_array):
    if x <= x_array[1]:
        return 0
    elif x >= x_array[len(x_array) - 1]:
        return len(x_array) - 2
    for i in range(2, len(x_array)):
        if x_array[i - 1] <= x <= x_array[i]:
            return i - 1


def piecewise_linear_interpolation(data_xy, x_array,
                                   print_process: bool = False):
    ab_matrix = []
    y_array = []
    for i in range(len(data_xy) - 1):
        ab_data_xy = [data_xy[i], data_xy[i + 1]]
        ab_matrix.append(line_equation_get_ab(ab_data_xy, print_process))

    x_segments = get_column(data_xy, 0)
    for x in x_array:
        diapason = get_diapason(x, x_segments)
        y_array.append(line_equation_get_y(x, ab_matrix[diapason]))
    return y_array
