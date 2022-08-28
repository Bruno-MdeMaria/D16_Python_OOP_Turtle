import turtle as t
import random

samy = t.Turtle()   #CHAMAR TODOS OS MODOS
t.colormode(255)
samy.shape("turtle")
samy.color("dodger blue")
samy.penup()
samy.sety(100)
samy.setx(20-100)
samy.pendown()
samy.pensize(10)

def random_cor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color









t.Screen()
t.exitonclick()

