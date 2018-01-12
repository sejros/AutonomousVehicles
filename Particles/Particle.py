# coding=utf-8

import random
from abc import abstractmethod, ABCMeta
from math import pi
from numpy import array as vector
import numpy as np

import pygame

try:
    from Box2D import b2PolygonShape, b2CircleShape
except ImportError:
    def b2PolygonShape(*args, **kwargs):
        raise NotImplementedError()


    def b2CircleShape(*args, **kwargs):
        raise NotImplementedError()

from chp06_agents.Particles.Globals import vec_pixels2world, vec_world2pixels, scalar_pixels2world, WIDTH, HEIGHT


class Sprite(metaclass=ABCMeta):
    def __init__(self):
        self.lifespan = 150
        self.age = self.lifespan

    @abstractmethod
    def draw(self, scr):
        pass

    @abstractmethod
    def delete(self, world):
        pass

    @abstractmethod
    def apply(self, force):
        pass


class Mover(Sprite):
    def __init__(self, pos):
        super().__init__()
        spread = 10.0
        self.position = pos
        self.velocity = np.array([random.uniform(-spread, spread),
                                  random.uniform(-spread, spread)])
        self.acceleration = np.array([0.0, 0.0])
        self.mover = None
        self.mass = 1.0
        # self.mass = random.uniform(0.5, 2.0)
        self.radius = 5 * self.mass
        self.size = vector([random.random() * 10 + 10, random.random() * 5 + 5])

    def apply(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = np.array([0.0, 0.0])

        self.age -= 1

    def draw(self, scr):
        s = pygame.Surface(self.size, pygame.SRCALPHA)  # per-pixel alpha
        color = (self.age / self.lifespan) * 255
        print(self.age, self.lifespan, color)
        s.fill((127, 127, 127, color))  # notice the alpha value in the color
        # pygame.draw.rect(s, (0, 0, 0),
        #                  [0, 0,
        #                   self.size[0], self.size[1]], 3)
        # s = pygame.transform.rotate(s, 45)
        scr.blit(s, self.position)

    def delete(self, world):
        pass

    def bounce(self):
        if 0 > self.position[0]:
            self.position[0] = 0
            self.velocity[0] *= -1
        if self.position[0] > WIDTH:
            self.position[0] = WIDTH
            self.velocity[0] *= -1
        if 0 > self.position[1]:
            self.position[1] = 0
            self.velocity[1] *= -1
        if self.position[1] > HEIGHT:
            self.position[1] = HEIGHT
            self.velocity[1] *= -1

    def toroid(self):
        self.position[0] %= WIDTH
        self.position[1] %= HEIGHT

    def run(self, scr):
        self.update()
        self.toroid()
        self.draw(scr)


# TODO from chapter 4 and 3

class Particle(Sprite):
    def __init__(self, world, pos, size=None):
        super().__init__()
        pos = vec_pixels2world(pos)

        self.size = (random.random() * 10 + 5, random.random() * 10 + 5)
        if size:
            self.size = size

        # shape = b2CircleShape(pos=(pos[0], pos[1]), radius=scalar_pixels2world(size*2))
        shape = b2PolygonShape(box=(scalar_pixels2world(self.size[0] / 2),
                                    scalar_pixels2world(self.size[1] / 2)))

        self.body = world.CreateDynamicBody(position=(pos[0], pos[1]),
                                            shapes=shape)
        self.box = self.body.CreateCircleFixture(shape=shape, density=1.0, friction=0.1)

        self.pos = self.body.position

    def draw(self, scr):
        s = pygame.Surface(self.size, pygame.SRCALPHA)  # per-pixel alpha
        s.fill((127, 127, 127, int((255.0 / self.lifespan) * self.age)))  # notice the alpha value in the color
        pygame.draw.rect(s, (0, 0, 0, int((255.0 / self.lifespan) * self.age)),
                         [0, 0,
                          self.size[0], self.size[1]], 3)
        s = pygame.transform.rotate(s, self.body.angle * 180 / pi)

        pos = vec_world2pixels(self.body.position)
        pos = (pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2)
        scr.blit(s, pos)

    def delete(self, world):
        world.DestroyBody(self.body)
        pass

    def apply(self, force):
        raise NotImplementedError()
        pass
