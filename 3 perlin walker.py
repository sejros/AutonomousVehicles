# coding=utf-8

from tkinter import *
import random
import noise
from math import sqrt

WIDTH = 800.0
HEIGHT = 600.0


class Walker:
    def __init__(self):
        self.pos = [WIDTH / 2, HEIGHT / 2]
        self.vel = [0, 0]
        self.BALL_RADIUS = 6
        self.BALL_SPEED = 25
        self.seed1 = random.random()
        self.seed2 = random.random()
        self.mover = c.create_oval(self.pos[0] - self.BALL_RADIUS / 2,
                                   self.pos[1] - self.BALL_RADIUS / 2,
                                   self.pos[0] + self.BALL_RADIUS / 2,
                                   self.pos[1] + self.BALL_RADIUS / 2,
                                   fill="black")

    def draw(self, canvas):
        canvas.delete(self.mover)
        oval = canvas.create_oval(self.pos[0] - self.BALL_RADIUS / 2,
                                  self.pos[1] - self.BALL_RADIUS / 2,
                                  self.pos[0] + self.BALL_RADIUS / 2,
                                  self.pos[1] + self.BALL_RADIUS / 2,
                                  fill="black")
        self.mover = oval

    def update(self, trail=False):
        x = (noise.pnoise1(self.seed1) + 1) * WIDTH / 2
        y = (noise.pnoise1(self.seed2) + 1) * HEIGHT / 2

        self.seed1 += 0.001 * sqrt(2) * self.BALL_SPEED
        self.seed2 += 0.001 * sqrt(2) * self.BALL_SPEED

        if trail:
            c.create_line(self.pos[0], self.pos[1],
                          x, y,
                          width=self.BALL_RADIUS / 4, fill="red")

        self.pos[0] = x
        self.pos[1] = y


root = Tk()
root.title("Tkinter demo")

# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#ffffff")
c.pack()

mover = Walker()


def draw():
    mover.update(True)
    mover.draw(c)
    root.after(25, draw)  # 40 fps


draw()

root.mainloop()
