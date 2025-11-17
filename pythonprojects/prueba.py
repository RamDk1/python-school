# Illustrate calling a turtle function
# Ramses Rodriguez

import turtle

# Define functions
def drawPolygon(t, angle):
    """
    Draws a pentagon-like shape using the given turtle and angle.

    Parameters:
    t (Turtle): The turtle object used for drawing.
    angle (int): The angle to turn after drawing each side
    """
    sides = 5
    side_length = 100  # Length of each side
    for i in range(sides):
        t.forward(side_length)
        t.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("pink")

    # Drawing the pentagons with different angles
    alex = turtle.Turtle()
    drawPolygon(alex, 72)   # Standard pentagon
    alex.penup()
    alex.goto(-150, 0)      # Move turtle to a new position
    alex.pendown()
    drawPolygon(alex, 90)   # Draw a square
    alex.penup()
    alex.goto(150, 0)       # Move turtle to another position
    alex.pendown()
    drawPolygon(alex, 144)  # Draw a star-like shape

    wn.exitonclick()

# Call main function
main()
