# coding=utf-8

import random
from .Particle import Particle


class ParticleSystem:
    def __init__(self, world, pos):
        self.pos = pos
        self.world = world
        self.particles = []

    def draw(self, c):
        for particle in self.particles:
            particle.draw(c)

    def update(self):
        if random.random() < 0.5:
            self.particles.append(Particle(self.world, self.pos.copy()))

        for particle in self.particles:
            particle.life -= 1
            if particle.life <= 0:
                particle.delete(self.world)
                self.particles.remove(particle)

    def run(self, c):
        self.update()
        self.draw(c)
