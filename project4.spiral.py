import turtle as t
import random

samy = t.Turtle()   #CHAMAR TODOS OS MODOS
t.colormode(255)
samy.speed(0)
samy.shape("turtle")
samy.color("dodger blue")
samy.penup()
samy.sety(50)
samy.setx(20-100)
samy.pendown()
samy.pensize()


#um espirografico:

def random_cor():                    #função para definir uma cor aleatória baseada em RGB
    r = random.randint(0,255)        #defini as cores red, green e blue de 0 a 255 como no HTML/CSS
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)        #variavel recebe uma tuble
    return random_color             #a função retorna a variável.

def desenho_espirografico(largura_do_intervalo):         #para parar precisamente é preciso de uma função
    for _ in range(int(360 / largura_do_intervalo)):     #terá um loop de laço do tamnho de uma volta(360) / largura de uma linha a outra.
        samy.color(random_cor())                         #chamar a função random_cor() no método t.color()    
        samy.circle(100)                                 #o método circle com a quantidade de passos(tamanho)
        samy.setheading(samy.heading()+5)                #é o indice de inlinação da t. o heading recebe a posição atual da inclinação e acrescenta +5.

desenho_espirografico(5)   #chamar a função colocando como parametro a largura desejada entre as linhas.



t.Screen()
t.exitonclick()

