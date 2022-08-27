from turtle import Turtle, Screen
import random

samy = Turtle()               #CHAMANDO O OBJETO
samy.shape("turtle")          #MUDANDO A FORMA 
samy.color("dodger blue")     #ALTERANDO A COR
                              
                              #SCREM no final do programa


samy.penup()                  #REGULANDO A POSIÇÃO INICIAL - PRIMEIRO MÉTODO
samy.sety(100)                #posição y e x no screm
samy.setx(20-100)
samy.pendown()                

lista_cores = ["medium blue", "lime", "dark magenta", "gold", "orange red", "blue violet", "dark green", "red"]

def voltas(num_lados):          #a função voltas com o parametro número de lados para ser chamada no loop posterior
    angulo = 360 / num_lados    #para fazer um desenho iniciando de um triangulo até um decágono.
    for _ in range(num_lados):  #loop tera o numero de lados do parametro quando a função for chamada posteriormente
        samy.forward(100)       #mivimento de 100 passos para frente
        samy.rt(angulo)         #virar para direita(rt) no angulo definido pelo 360 / numero de lados que queremos

for range_lado in range(3,11):       #loop iniciará movimentando 3 vezes(triangulo) até 10 vezes(11-1) decagóno.
    samy.color(random.choice(lista_cores))#mudará de cor a cada loop conforme uma escolha aleatoria da lista de cores
    voltas(range_lado)               #loop chamará a função que adotará como parametro o range que estará passando.


    #ABAIXO OUTRAS FORMAS E MOVIMENTOS.


# for _ in range(4):
#     samy.forward(100)
#     samy.rt(90)

# for _ in range(10):
#     samy.forward(10)
#     samy.penup()
#     samy.forward(10)
#     samy.pendown()


# for _ in range(3):
#     samy.forward(100)
#     samy.rt(120)

# num_lados = 2
# for _ in range(3,11):
#     num_lados +=1
#     angulo = 360 / num_lados
#     for _ in range(num_lados):
#         samy.forward(100)
#         samy.rt(angulo)

  


screm = Screen()
screm.exitonclick()

