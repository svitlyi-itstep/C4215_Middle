import turtle as t
import random


def draw_rectangle():
    for i in range(4):
        if i % 2 == 0:
            t.forward(200)
        else:
            t.forward(100)
        t.left(90)


def draw_square(length, color):
    t.color(color)
    for i in range(4):
        t.forward(length)
        t.left(90)


t.reset()
screen = t.Screen()
t.speed(10)

for i in range(24):
    length = random.randint(60, 140)
    color = random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'black'])
    draw_square(length, color)
    t.left(15)




screen.exitonclick()

