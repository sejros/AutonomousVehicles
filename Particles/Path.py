from math import sqrt

import pygame
from numpy import array as vector


class Path:
    def __init__(self):
        self.points = []
        self.raduis = 20

    def add_point(self, x, y):
        self.points.append(vector((int(x), int(y))))

    def draw(self, scr):
        for i in range(len(self.points) - 1):
            start = self.points[i]
            end = self.points[i + 1]
            pygame.draw.line(scr, (255, 230, 255),
                             start, end,
                             self.raduis * 2)
            pygame.draw.circle(scr, (255, 230, 255),
                               start, self.raduis)
            pygame.draw.circle(scr, (255, 230, 255),
                               end, self.raduis)

        for i in range(len(self.points) - 1):
            start = self.points[i]
            end = self.points[i + 1]
            pygame.draw.line(scr, (255, 0, 255), start, end, 2)

    def get_normal(self, pos, predict_rate=50):
        best_normal = None
        best_dist = -1

        eps = 0.01

        for i in range(len(self.points) - 1):
            start = self.points[i]
            end = self.points[i + 1]

            ab = end - start
            abn = ab / sqrt(ab[0] ** 2 + ab[1] ** 2)
            ap = pos - start

            normal = start + abn * (abn[0] * ap[0] + abn[1] * ap[1])
            future_normal = normal + abn * predict_rate

            ax = future_normal - start
            if ab[0] != 0:
                k = ax[0] / ab[0]
            else:
                k = ax[1] / ab[1]

            d = sqrt((normal[0] - pos[0]) ** 2 + ((normal[1] - pos[1]) ** 2))

            if not 0.0 - eps <= k <= 1.0 + eps:
                d += 10000

            if best_dist == -1 or d < best_dist:
                best_dist = d
                best_normal = future_normal

        return best_normal
