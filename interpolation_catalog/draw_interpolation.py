import matplotlib.pyplot as plt
import matplotlib.pyplot as pypl
import interpolation_catalog.interpolation as inp
import matrix_catalog.matrix as mx
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np


def draw_grid(fig, ax, title):
    ax.set_title(title, fontsize=16)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)

    ax.grid(which='major', linewidth=1.5)
    ax.grid(which='major', linestyle='--', color="gray", linewidth=0.5)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)


def draw_graph_interpolation(title, coefficents, data_xy, data_x, data_y):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    x = [data_xy[0][0], data_xy[1][0]]
    y = [data_xy[0][1], data_xy[1][1]]

    ax.plot(x, y, label=f"y = {coefficents[0]}*x + {coefficents[1]}")
    ax.scatter(data_x, data_y, c="red")
    ax.legend()

    plt.show()


def draw_graph_pl_interpolation(title, data_xy, data_x, data_y):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    x_segments = mx.get_column(data_xy, 0)
    y_segments = mx.get_column(data_xy, 1)

    ax.plot(x_segments, y_segments)
    ax.scatter(data_x, data_y, c="red")
    ax.legend()

    plt.show()


def draw_graph_lagrange(title, data_xy):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    data_x = np.arange(1, 7, 0.05)
    data_y = []
    for x in data_x:
        data_y.append(inp.lagrange_polynomial(data_xy, x))

    x_segments = mx.get_column(data_xy, 0)
    y_segments = mx.get_column(data_xy, 1)

    ax.plot(data_x, data_y)
    ax.scatter(x_segments, y_segments)
    ax.legend()

    plt.show()
