from turtle import Turtle, Screen

samy = Turtle()
samy.shape("turtle")
samy.color("dodger blue")


# for _ in range(4):
#     samy.forward(100)
#     samy.rt(90)

for _ in range(10):
    samy.forward(10)
    samy.penup()
    samy.forward(10)
    samy.pendown()



screm = Screen()
screm.exitonclick()

