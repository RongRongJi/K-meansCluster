# utf-8
import numpy as np
import matplotlib.pyplot as plt

def draw_point(points, colors):
    xs, ys = [], []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    plt.scatter(xs, ys, c=colors)