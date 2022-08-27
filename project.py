from turtle import Turtle, Screen

samy = Turtle()
samy.shape("turtle")
samy.color("dodger blue")


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

samy.penup()
samy.sety(100)
samy.setx(20-100)
samy.pendown()
def voltas(num_lados):
    angulo = 360 / num_lados
    for _ in range(num_lados):
        samy.forward(100)
        samy.rt(angulo)

for range_lado in range(3,11):
    voltas(range_lado)




  





screm = Screen()
screm.exitonclick()

