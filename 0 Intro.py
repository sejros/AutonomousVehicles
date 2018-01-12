# coding=utf-8

from tkinter import *
import random

WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 3
BALL_SPEED = 1

root = Tk()
root.title("Tkinter demo")

# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#ffffff")
c.pack()


mover = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                      HEIGHT/2-BALL_RADIUS/2,
                      WIDTH/2+BALL_RADIUS/2,
                      HEIGHT/2+BALL_RADIUS/2, fill="black")


def mover_move():
    rand = random.random()
    if rand < 0.25:
        c.move(mover, 0, BALL_SPEED)
    elif 0.25 <= rand < 0.5:
        c.move(mover, 0, -BALL_SPEED)
    elif 0. <= rand < 0.75:
        c.move(mover, BALL_SPEED, 0)
    elif 0.75 <= rand:
        c.move(mover, -BALL_SPEED, 0)


def main():
    mover_move()
    root.after(25, main)    # 40 fps


main()

root.mainloop()
