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
lista_direcoes = [0, 90, 180, 270]


for _ in range(200):
    samy.color(random.choice(lista_cores))
    samy.forward(30)
    samy.setheading(random.choice(lista_direcoes))




screm = Screen()
screm.exitonclick()

