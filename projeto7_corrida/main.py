from turtle import Turtle, Screen, speed
import random
import turtle

corrida_on = False           #para a corrida não cmeçar imediantamente antes do usuario apostar
screen = Screen()
screen.setup(width= 500, height= 400)    #altura e  largura do screen



aposta = screen.textinput(title="Faça sua aposta", prompt="Qual a cor da tartaruga que você quer apostar? ")
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
lista_posicao = [-80, -40, 0, 40 , 80, 120]
lista_turtle = []

for tartaruga_posicao in range(0,6):
    nova_turtle = Turtle(shape="turtle")
    nova_turtle.speed("slow")
    nova_turtle.color(cores[tartaruga_posicao])
    nova_turtle.penup()
    nova_turtle.goto(x= -230, y= lista_posicao[tartaruga_posicao])
    lista_turtle.append(nova_turtle)

if aposta:
    corrida_on = True      #para iniciar somente depois do imput de aposta do usuário

while corrida_on:
    for tartaruga in lista_turtle:
        if turtle.xcor() > 230:         # xcor é a cordernada x do screm. lembrando que tem 500 no total -250 e 250.
            corrida_on = False
            cor_vencedora = turtle.pencolor() #quando for maior que 230 ou seja ganhou, dederá então cor_vencedora receber a cor da tartaruga em questão.
            if cor_vencedora == aposta:
                print(f"A tartaruga {cor_vencedora} chegou primeiro. Você venceu!")
            else:
                print(f"A tartaruga {cor_vencedora} chegou primeiro. Você perdeu!")     
        passos = random.randint(0,10)   # umm número aleatório entre 0 e 10
        tartaruga.forward(passos)


screen.exitonclick()