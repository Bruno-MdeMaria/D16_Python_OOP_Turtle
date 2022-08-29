
import turtle as t
import random

samy = t.Turtle()   #CHAMAR TODOS OS MODOS
t.colormode(255)     #tem que alterar o modo cor para 255
samy.speed(0)
samy.shape("turtle")
samy.color("dodger blue")
samy.penup()
samy.sety(50)
samy.setx(20-100)
samy.pendown()
samy.pensize()

cores = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210), (77, 37, 76), (120, 117, 155), (35, 35, 35)]

for _ in range(10):
    samy.dot(20, random.choice(cores))
    samy.forward(50)




t.Screen()
t.exitonclick()

