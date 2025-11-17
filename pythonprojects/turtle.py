import turtle

# Crear la tortuga
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)  # Velocidad de dibujo (1 es lento, 10 es rápido)

# Función para dibujar una flor
def dibujar_flor(tortuga, radio, color):
    tortuga.color(color)
    for _ in range(36):
        tortuga.circle(radio, 60)  # Dibuja un pétalo
        tortuga.left(10)  # Gira la tortuga para crear los pétalos

# Función para dibujar una flor en una posición específica
def flor(x, y, radio, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    dibujar_flor(t, radio, color)

# Dibujar varias flores en distintas posiciones
flor(-150, 100, 50, "red")
flor(100, 150, 60, "yellow")
flor(-200, -100, 40, "blue")
flor(150, -150, 70, "purple")

# Ocultar la tortuga después de dibujar
t.hideturtle()

# Esperar a que el usuario haga clic para cerrar
turtle.done()
