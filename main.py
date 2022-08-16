# import turtle - PODEMOS IMPORTAR DESTA FORMA E DAI PRECIISAMOS IMPORTAR A CLASSE COMO A FUNÇÃO ABAIXO:

# samy = turtle.Turtle()

# OU ASSIM:


from turtle import Screen, Turtle
import turtle

samy = Turtle()
samy.shape("turtle")
samy.color("coral","green")
turtle.forward(100)

my_screnn = Screen()
my_screnn.exitonclick()