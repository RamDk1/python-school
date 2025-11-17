import turtle
import random

class StampTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()

    # Override forward method to spin and stamp
    def forward(self, dist):
        self.right(360)
        super().forward(dist)
        self.stamp()

    # Override backward method to change color after every move
    def backward(self, dist):
        super().backward(dist)
        self.color(random.choice(['red', 'green', 'blue', 'yellow']))

# Create your own turtle class with different behavior
class CustomTurtle(turtle.Turtle):
    # Constructor - define custom turtle behavior
    def __init__(self):
        super().__init__()

    # Override forward method to change pen size
    def forward(self, dist):
        self.pensize(random.randint(1, 10))  # Random pen size each time
        super().forward(dist)

    # Override backward method to change shape of stamp
    def backward(self, dist):
        self.shape(random.choice(['turtle', 'triangle', 'square', 'circle']))
        super().backward(dist)

def main():
    # Named constants
    screen_size = 500
    screen_startx = 60  # x coordinate of the left edge of the graphics window

    # Set up the window and its attributes
    wn = turtle.Screen()
    wn.setup(screen_size, screen_size, screen_startx, 0)
    turtle_list = []
    num_turtles = 2
    num_stamp_turtles = 3
    num_custom_turtles = 2  # Adding two custom turtles

    # Create a list of different colored turtles, each pointing in a different direction
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.color(random.choice(['red', 'green', 'blue', 'yellow']))
        turtle_list.append(t)

    # Create a list of different colored stamp_turtles, each pointing in a different direction
    for _ in range(num_stamp_turtles):
        t = StampTurtle()
        t.right(random.randrange(350))
        t.color('black')
        turtle_list.append(t)

    # Create a list of custom turtles with unique behavior
    for _ in range(num_custom_turtles):
        t = CustomTurtle()
        t.right(random.randrange(350))
        t.color('purple')  # Give custom turtles a unique color
        turtle_list.append(t)

    # Move each turtle outward from the origin ten times
    for t in turtle_list:
        for _ in range(10):
            t.forward(random.randrange(10, 30))

    wn.exitonclick()

# Run the main function. This should be the last statement in the file.
main()
