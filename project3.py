from turtle import Turtle, Screen
import random

samy = Turtle()
samy.shape("turtle")
samy.color("dodger blue")

samy.penup()
samy.sety(100)
samy.setx(20-100)
samy.pendown()
samy.pensize(10)

lista_cores = ["medium blue", "lime", "dark magenta", "gold", "orange red", "blue violet", "dark green", "red"]
lista_movimentos = [samy.forward(10), samy.rt(90)]

for _ in range(100):
    samy.color(random.choice(lista_cores))
    random.choice(lista_movimentos)




screm = Screen()
screm.exitonclick()

