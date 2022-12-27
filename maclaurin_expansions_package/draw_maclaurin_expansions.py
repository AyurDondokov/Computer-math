import matplotlib.pyplot as plt
import maclaurin_expansions_package.maclaurin_expansions as me

def draw_maclaurin_function(title, range_of_func, func, n):
    masX = []
    masY = []
    for i in range(range_of_func[0], range_of_func[1]):
        masX.append(func(i / 10, n))
    for i in range(range_of_func[0], range_of_func[1]):
        masY.append(i/10)
    print(masX)
    plt.axhline(0, color='black', lw=1.0)
    plt.axvline(0, color='black', lw=1.0)
    plt.plot(masY, masX, color='orange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.show()


def test_draw_maclaurin_function():
    draw_maclaurin_function("get e", (-10, 10), me.get_maclaurin_arcsin, 2)