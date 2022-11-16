import math
EPS = 1E-5


def sub(x):
    return x[0]-x[1]


def mul(x):
    return x[0]*x[1]


def print_vector(self):
    """Красивый вывод вектора"""
    s = "("
    for i in self:
        s += str(i) + "; "
    print(s[:-2]+")")


def sum_of_scalar(v1, other):
    """Сложение со скаляром"""
    if len(v1) == len(other):
        return list(map(sum, zip(v1, other)))
    else:
        raise ValueError('Разномерные вектора')


def sub_of_scalar(v1, other):
    """Вычитание скаляра"""
    if len(v1) == len(other):
        return list(map(sub, zip(v1, other)))
    else:
        raise ValueError('Разномерные вектора')


def mul_on_scalar(v1, scalar):
    """Умножение на скаляр"""
    return list(i * scalar for i in v1)


def dif_on_scalar(v1, scalar):
    """Делание на скаляр"""
    return list(i / scalar for i in v1)


def scalar_mul(v1, other):
    """Скалярное умножение"""
    if len(v1) == len(other):
        return sum(map(mul, zip(v1, other)))
    else:
        raise ValueError('Разномерные вектора')


def is_colineal(v1, other):
    """Проверка на коллиниальность"""
    if len(v1) == len(other):
        return is_scalar_almost_equals(cos(v1, other), 1)
    else:
        raise ValueError('Разномерные вектора')


def angle_bet_vectors(m1, other):
    """Угол между векторами в градусах"""
    rad_angle = math.acos(scalar_mul(m1, other) / (length(m1) * length(other)))
    return (rad_angle*180)/math.pi


def is_codirection(m1, other):
    """Проверка на сонаправленность"""
    if len(m1) == len(other):
        return is_scalar_almost_equals(angle_bet_vectors(m1, other), 0)
    else:
        raise ValueError('Разномерные вектора')


def is_antidirection(v1, other):
    """Проверка на противонаправленность"""
    if len(v1) == len(other):
        return is_scalar_almost_equals(cos(v1, other), -1)
    else:
        raise ValueError('Разномерные вектора')


def length(v1):
    """Длина вектора"""
    return math.sqrt(scalar_mul(v1, v1))


def is_equals(v1, other):
    """Проверка на равенство"""
    if len(v1) == len(other):
        for i in range(0, len(v1)):
            if v1[i] != other[i]:
                return False
        return True
    else:
        raise ValueError('Разномерные вектора')


def cos(v1, other):
    """Косинус двух векторов"""
    if len(v1) == len(other):
        return scalar_mul(v1, other) / (length(v1) * length(other))
    else:
        raise ValueError('Разномерные вектора')


def is_ortogon(v1, other):
    """Проверка на ортогональность"""
    if len(v1) == len(other):
        return is_scalar_almost_equals(angle_bet_vectors(v1, other), 90)
    else:
        raise ValueError('Разномерные вектора')


def is_scalar_almost_equals(a, b, eps=EPS):
    """Равенство скаляров с заданной точностью"""
    return abs(a - b) <= eps


def is_vectors_almost_equals(v1, other, eps=EPS):
    """Равенство векторов с заданной точностью"""
    if len(v1) == len(other):
        return False not in [is_scalar_almost_equals(va, vb, eps) for va, vb in zip(v1, other)]
    else:
        raise ValueError('Разномерные вектора')


def scalar_projection(v1, other):
    """Скалярная проекция вектора"""
    if len(v1) == len(other):
        return scalar_mul(v1, other) / length(other)
    else:
        raise ValueError('Разномерные вектора')


def vector_projection(v1, other):
    """Векторная проекция вектора"""
    if len(v1) == len(other):
        return mul_on_scalar(other, scalar_mul(v1, other) / scalar_mul(other, other))
    else:
        raise ValueError('Разномерные вектора')
