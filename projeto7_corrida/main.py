from turtle import Turtle, Screen


screen = Screen()
screen.setup(width= 500, height= 400)    #altura e  largura do screen

aposta = screen.textinput(title="Faça sua aposta", prompt="Qual a cor da tartaruga que você quer apostar? ")


samy = Turtle(shape="turtle")
samy.penup()
samy.goto(x= -230, y= -100)

screen.exitonclick()