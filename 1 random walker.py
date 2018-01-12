# coding=utf-8

from tkinter import *
import random


WIDTH = 800
HEIGHT = 600


class Walker:
    def __init__(self):
        self.pos = [WIDTH / 2, HEIGHT / 2]
        self.vel = [0, 0]
        self.BALL_RADIUS = 6
        self.BALL_SPEED = 2
        self.mover = c.create_oval(self.pos[0] - self.BALL_RADIUS / 2,
                                   self.pos[1] - self.BALL_RADIUS / 2,
                                   self.pos[0] + self.BALL_RADIUS / 2,
                                   self.pos[1] + self.BALL_RADIUS / 2, fill="black")

    def update(self, trail=False):
        rand = random.random()
        if rand < 0.25:
            self.vel = (0, self.BALL_SPEED)
        elif 0.25 <= rand < 0.5:
            self.vel = (0, -self.BALL_SPEED)
        elif 0.5 <= rand < 0.75:
            self.vel = (self.BALL_SPEED, 0)
        elif 0.75 <= rand:
            self.vel = (-self.BALL_SPEED, 0)

        if trail:
            c.create_line(self.pos[0], self.pos[1],
                          self.pos[0] + self.vel[0],
                          self.pos[1] + self.vel[1],
                          width=self.BALL_RADIUS / 4, fill="red")

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        c.delete(self.mover)
        self.mover = c.create_oval(self.pos[0] - self.BALL_RADIUS / 2,
                                   self.pos[1] - self.BALL_RADIUS / 2,
                                   self.pos[0] + self.BALL_RADIUS / 2,
                                   self.pos[1] + self.BALL_RADIUS / 2, fill="black")


root = Tk()
root.title("Tkinter demo")

# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#ffffff")
c.pack()

mover = Walker()


def main():
    mover.update(True)
    root.after(25, main)  # 40 fps


main()

root.mainloop()
