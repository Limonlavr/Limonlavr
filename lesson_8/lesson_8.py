# imprort random# подтянуть в проект random
# import random as r  # библиотек под именем r
#
# # from random import randint
# x = r.randint(0, 100)
# from random import *  # так луче не делать
#
# x = randint(0, 100)  # от 0 до 100
# lst = [0, 1, 2, 3, 4, 5]
# lst = r.shuffle(lst)
#
# print(x)
# print(lst)

import turtle

t = turtle.Turtle()
t.penup()
t.goto(200, 200) # x(горизонталь),у(вертикаль)
screen = turtle.Screen()
t.color()
t.pensize(5)  # толшина
# 1 - самая медлиная
# 10 - очень быстро
# 0 - максимальная скорость
t.speed(1)  # speed изменение скорости
gorioal = 150
k = 300

t.forward(gorioal) # вперёд на 50 пикселей
t.right(90) # поворот на 90 градусов
t.forward(gorioal)
t.right(90)
t.forward(k)
t.right(90)
t.forward(gorioal)
t.right(90)

t.end_fill()
screen.exitonclick()
