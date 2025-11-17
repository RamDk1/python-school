import random
import turtle

# Ramses Rodriguez
# 11/11/2024

# Function: isInScreen
# Parameters:
#   win - the turtle screen object
#   turt - the turtle object to check
# Returns:
#   A boolean value indicating whether the turtle is still within the screen boundaries.

def isInScreen(win, turt):
    # Define the screen boundaries
    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    # Get the turtle's current position
    turtleX = turt.xcor()
    turtleY = turt.ycor()

    # Determine if the turtle is still within the bounds
    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

# Function: moveRandomly
# Parameters:
#   turt - the turtle object to move
#   distance - the distance the turtle moves
# Description:
#   Moves the turtle randomly by turning left or right and then moving forward by the given distance.

def moveRandomly(turt, distance):
    coin = random.randrange(0, 2)  # Randomly choose between 0 and 1
    if coin == 0:
        turt.left(90)  # Turn left if coin is 0
    else:
        turt.right(90)  # Turn right if coin is 1
    turt.forward(distance)  # Move forward by the given distance

# Main Program
def main():
    # Initialize the screen and turtles
    wn = turtle.Screen()
    wn.title("Random Turtle Movement")

    june = turtle.Turtle()
    june.shape('turtle')
    june.color("blue")  # Set color for the first turtle
    june.penup()
    june.goto(-100, 0)  # Start the first turtle at a specific location
    june.pendown()

    lily = turtle.Turtle()
    lily.shape('turtle')
    lily.color("green")  # Set color for the second turtle
    lily.penup()
    lily.goto(100, 0)  # Start the second turtle at a different location
    lily.pendown()

    # Loop until the first turtle exits the screen
    while isInScreen(wn, june):
        moveRandomly(june, 50)  # Move the first turtle
        for _ in range(5):
            if isInScreen(wn, lily):
                moveRandomly(lily, 10)  # Move the second turtle 5 times with a shorter distance

    # Determine which turtle is higher on the screen
    if june.ycor() > lily.ycor():
        higher_turtle = june
        higher_name = "June"
    else:
        higher_turtle = lily
        higher_name = "Lily"

    # Display the result
    higher_turtle.penup()
    higher_turtle.goto(0, 0)
    higher_turtle.write(f"{higher_name} is higher on the screen!", align="center", font=("Arial", 16, "bold"))

    # Close the screen on click
    wn.exitonclick()

# Run the main program
main()
