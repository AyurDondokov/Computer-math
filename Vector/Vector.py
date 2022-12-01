import math
EPS = 1E-5


def sub(x):
    return x[0]-x[1]


def mul(x):
    return x[0]*x[1]


def print_vector(vector):
    """Красивый вывод вектора"""
    s = "("
    for i in vector:
        s += str(i) + "; "
    print(s[:-2]+")")


def sum_of_scalar(vector_1, vector_2):
    """Сложение со скаляром"""
    if len(vector_1) == len(vector_2):
        return list(map(sum, zip(vector_1, vector_2)))
    else:
        raise ValueError('Разномерные вектора')


def sub_of_scalar(vector_1, vector_2):
    """Вычитание скаляра"""
    if len(vector_1) == len(vector_2):
        return list(map(sub, zip(vector_1, vector_2)))
    else:
        raise ValueError('Разномерные вектора')


def mul_on_scalar(vector_1, vector_2):
    """Умножение на скаляр"""
    return list(i * vector_2 for i in vector_1)


def dif_on_scalar(vector, scalar):
    """Делание на скаляр"""
    return list(i / scalar for i in vector)


def scalar_mul(vector_1, vector_2):
    """Скалярное умножение"""
    if len(vector_1) == len(vector_2):
        return sum(map(mul, zip(vector_1, vector_2)))
    else:
        raise ValueError('Разномерные вектора')


def is_colineal(vector_1, vector_2):
    """Проверка на коллиниальность"""
    if len(vector_1) == len(vector_2):
        return are_scalars_almost_equals(cos(vector_1, vector_2), 1)
    else:
        raise ValueError('Разномерные вектора')


def angle_bet_vectors(vector_1, vector_2):
    """Угол между векторами в градусах"""
    rad_angle = math.acos(scalar_mul(vector_1, vector_2) / (length(vector_1) * length(vector_2)))
    return (rad_angle*180)/math.pi


def is_co_direction(vector_1, vector_2):
    """Проверка на сонаправленность"""
    if len(vector_1) == len(vector_2):
        return are_scalars_almost_equals(angle_bet_vectors(vector_1, vector_2), 0)
    else:
        raise ValueError('Разномерные вектора')


def is_counter_direction(vector_1, vector_2):
    """Проверка на противонаправленность"""
    if len(vector_1) == len(vector_2):
        return are_scalars_almost_equals(cos(vector_1, vector_2), -1)
    else:
        raise ValueError('Разномерные вектора')


def length(vector):
    """Длина вектора"""
    return math.sqrt(scalar_mul(vector, vector))


def is_equals(vector_1, vector_2):
    """Проверка на равенство"""
    if len(vector_1) == len(vector_2):
        for i in range(0, len(vector_1)):
            if vector_1[i] != vector_2[i]:
                return False
        return True
    else:
        raise ValueError('Разномерные вектора')


def cos(vector_1, vector_2):
    """Косинус двух векторов"""
    if len(vector_1) == len(vector_2):
        return scalar_mul(vector_1, vector_2) / (length(vector_1) * length(vector_2))
    else:
        raise ValueError('Разномерные вектора')


def is_orthogonal(vector_1, vector_2):
    """Проверка на ортогональность"""
    if len(vector_1) == len(vector_2):
        return are_scalars_almost_equals(angle_bet_vectors(vector_1, vector_2), 90)
    else:
        raise ValueError('Разномерные вектора')


def are_scalars_almost_equals(scalar_1, scalar_2, eps=EPS):
    """Равенство скаляров с заданной точностью"""
    return abs(scalar_1 - scalar_2) <= eps


def are_vectors_almost_equals(vector_1, vector_2, eps=EPS):
    """Равенство векторов с заданной точностью"""
    if len(vector_1) == len(vector_2):
        return False not in [are_scalars_almost_equals(va, vb, eps) for va, vb in zip(vector_1, vector_2)]
    else:
        raise ValueError('Разномерные вектора')


def scalar_projection(vector_1, vector_2):
    """Скалярная проекция вектора"""
    if len(vector_1) == len(vector_2):
        return scalar_mul(vector_1, vector_2) / length(vector_2)
    else:
        raise ValueError('Разномерные вектора')


def vector_projection(vector_1, vector_2):
    """Векторная проекция вектора"""
    if len(vector_1) == len(vector_2):
        return mul_on_scalar(vector_2, scalar_mul(vector_1, vector_2) / scalar_mul(vector_2, vector_2))
    else:
        raise ValueError('Разномерные вектора')
