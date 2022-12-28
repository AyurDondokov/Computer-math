import math


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def get_maclaurin_e(x, n):
    e = 0
    for i in range(n, -1, -1):
        if i == 0:
            e += 1
        else:
            e += (x ** i) / factorial(i)
    return e


def get_maclaurin_sin(x, n):
    result = 0
    for i in range(n, -1, -1):
        if i == 0:
            result += x
        else:
            result += ((-1) ** i) * (x ** (2*i+1)) / factorial(2*i+1)
    return result


def get_maclaurin_cos(x, n):
    result = 0
    for i in range(n, -1, -1):
        if i == 0:
            result += 1
        else:
            result += ((-1) ** i) * (x ** (2*i)) / factorial(2*i)
    return result


def get_maclaurin_arcsin(x, n):
    result = 0
    for i in range(n, -1, -1):
        if i == 0:
            result += x
        else:
            result += (factorial(2*i) * (x ** (2*i+1))) / ((4 ** i) * (factorial(i) ** 2) * factorial(2*i+1))
    return result


def get_maclaurin_arccos(x, n):
    return math.pi/2 - get_maclaurin_arcsin(x, n)
