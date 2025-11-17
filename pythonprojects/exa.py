import turtle

def drawP(t, length):

    t.left(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)  
    t.forward(length)  
    t.left(90)
    t.forward(length)

t = turtle.Turtle()
drawP(t, 100)
turtle.done()
