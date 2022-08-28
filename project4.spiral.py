import turtle as t
import random

samy = t.Turtle()   #CHAMAR TODOS OS MODOS
t.colormode(255)
samy.shape("turtle")
samy.color("dodger blue")
samy.penup()
samy.sety(50)
samy.setx(20-100)
samy.pendown()
samy.pensize(3)


def random_cor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for _ in range(50):
    samy.color(random_cor())
    samy.circle(100)
    posicao = samy.heading()
    samy.setheading(posicao +10)






t.Screen()
t.exitonclick()

