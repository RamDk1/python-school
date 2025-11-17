# Ramses Rodriguez Barroso
# October 27, 2024
# The shape I made in this program was a house without doors and without windows, just the shape

import turtle
import random

wn = turtle.Screen()
wn.bgcolor ("lightblue")
ram = turtle.Turtle()
ram.speed(5)


# Here I used variables for all numbers
# I use the random method here so that the shape I draw is completely distorted.
side = random.randrange(50,100)
ltside = random.randrange(70,100)
bigside = random.randrange(100,170)
xtside = random.randrange(150,210)
sevside = random.randrange(40,70)


def draw_custom_shape(t):
    t.forward(side)
    t.left(ltside)
    t.forward(side)
    t.left(ltside)
    t.forward(side)
    t.left(ltside)
    t.forward(side)
    t.left(ltside)
    t.forward(side)
    t.left(ltside)
    t.forward(side)
    t.right(ltside)
    t.forward(side)
    t.left(bigside)
    t.forward(xtside)
    t.left(sevside)
    t.forward(bigside)
    t.left(138)
    t.forward(side)

# I made a loop here so I could draw 4 identical shapes
for i in range(4):
    draw_custom_shape(ram)
    ram.penup()
    ram.forward(300)
    ram.right(ltside)
    ram.pendown()


