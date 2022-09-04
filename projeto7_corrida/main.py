from turtle import Turtle, Screen
import random

corrida_on = False           #para a corrida não cmeçar imediantamente antes do usuario apostar
screen = Screen()
screen.setup(width= 500, height= 400)    #altura e  largura do screen



aposta = screen.textinput(title="Faça sua aposta", prompt="Qual a cor da tartaruga que você quer apostar? ")
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
lista_posicao = [-80, -40, 0, 40 , 80, 120]

for tartaruga_posicao in range(0,6):
    samy = Turtle(shape="turtle")
    samy.color(cores[tartaruga_posicao])
    samy.penup()
    samy.goto(x= -230, y= lista_posicao[tartaruga_posicao])

if aposta:
    corrida_on = True      #para iniciar somente depois do imput de aposta do usuário

while corrida_on:


screen.exitonclick()