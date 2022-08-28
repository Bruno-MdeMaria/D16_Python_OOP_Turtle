import turtle as t
import random

samy = t.Turtle()   #CHAMAR TODOS OS MODOS
t.colormode(255)


def random_cor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

samy.shape("turtle")
samy.color("dodger blue")

samy.penup()
samy.sety(100)
samy.setx(20-100)
samy.pendown()
samy.pensize(10)

#lista_cores = ["medium blue", "lime", "dark magenta", "gold", "orange red", "blue violet", "dark green", "red"]
lista_direcoes = [0, 90, 180, 270]


for _ in range(50):
    samy.color(random_cor())
    samy.forward(30)
    samy.setheading(random.choice(lista_direcoes))



t.Screen()
t.exitonclick()

