# coding=utf-8

from numpy.core.numeric import array as vector
from math import sqrt
from numpy.linalg import norm

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

mousepos = vector([WIDTH / 2, HEIGHT / 2])
is_mouse_down = False
is_rmouse_down = False

scale_factor = 10.0
transX = WIDTH / 2
transY = HEIGHT / 2


def vec_pixels2world(vec2):
    x, y = vec2[0], vec2[1]
    x_ = (x - transX) / scale_factor
    y_ = (transY - y) / scale_factor
    return x_, y_


def vec_world2pixels(vec2):
    x, y = vec2[0], vec2[1]
    x_ = x * scale_factor + transX
    y_ = (1 - y) * scale_factor + transY
    return x_, y_


def scalar_pixels2world(val):
    return val / scale_factor


def scalar_world2pixels(val):
    return val * scale_factor


def dist(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def normalize(vec):
    return vec / norm(vec)
