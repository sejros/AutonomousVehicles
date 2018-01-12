# coding=utf-8

import random

import numpy as np
import pygame
from numpy import array as vector

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

mousepos = np.array([WIDTH / 2, HEIGHT / 2])
is_mouse_down = False
is_rmouse_down = False


class Particle:
    def __init__(self, pos):
        spread = 1.0
        self.position = pos
        self.velocity = np.array([random.uniform(-spread, spread),
                                  random.uniform(-spread, spread)])
        self.acceleration = np.array([0.0, 0.0])
        self.mover = None
        self.mass = 1.0
        # self.mass = random.uniform(0.5, 2.0)
        self.radius = 5 * self.mass
        self.lifespan = 75
        self.size = vector([random.random() * 10 + 10, random.random() * 5 + 5])

    def apply(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = np.array([0.0, 0.0])

        self.lifespan -= 1

    def draw(self, scr):
        s = pygame.Surface(self.size, pygame.SRCALPHA)  # per-pixel alpha
        s.fill((127, 127, 127, (128 - self.lifespan)))  # notice the alpha value in the color
        pygame.draw.rect(s, (0, 0, 0, ((255 / 75) * self.lifespan)),
                         [0, 0,
                          self.size[0], self.size[1]], 3)
        # s = pygame.transform.rotate(s, 45)
        scr.blit(s, self.position)


class ParticleSystem:
    def __init__(self, pos):
        self.pos = pos.copy()
        self.particles = []

    def draw(self, c):
        for particle in self.particles:
            particle.draw(c)

    def update(self):
        self.particles.append(Particle(self.pos.copy()))

        for particle in self.particles:
            particle.update()
            if particle.lifespan <= 0:
                self.particles.remove(particle)

    def run(self, c):
        self.update()
        self.draw(c)

    def apply(self, force):
        for particle in self.particles:
            particle.apply(force)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
clock = pygame.time.Clock()

ps = ParticleSystem(vector([WIDTH / 2, 50]))


def main():
    global ps
    screen.fill(WHITE)

    ps.run(screen)

    for system in pss:
        system.run(screen)

    gravity = np.array([0, 0.1])
    ps.apply(gravity)
    for system in pss:
        system.apply(gravity)

    pygame.display.flip()
    clock.tick(60)

    # drag_coeff = -0.005
    # drag = drag_coeff * bob.velocity * np.linalg.norm(bob.velocity)
    # bob.apply(drag)


pss = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            mousepos = [event.pos[0], event.pos[1]]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_mouse_down = True
            pss.append(ParticleSystem(mousepos.copy()))
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_mouse_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            is_rmouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            is_rmouse_down = False
    main()
# root.mainloop()
