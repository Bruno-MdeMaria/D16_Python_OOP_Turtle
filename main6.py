import turtle as t


samy = t.Turtle()  #CHAMAR TODOS OS MODULOS PARA O OBJETO CRIADO SAMY

def mover_frente():
    samy.forward(10)

def mover_tras():
    samy.backward(10)

def mover_direita():
    samy.right(10)

def mover_esquerda():
    samy.left(10) 

def limpar():
    samy.clear()
    samy.penup()
    samy.home()
    samy.pendown()  


t.Screen()
t.listen()
t.onkey(key="w", fun= mover_frente)
t.onkey(key="s", fun= mover_tras)
t.onkey(key="d", fun= mover_direita)
t.onkey(key="a", fun= mover_esquerda)
t.onkey(key="c",fun= limpar)


t.Screen()  # CHAMAR O SCREEM E A SAIDA COM UM CLIQUE
t.exitonclick()