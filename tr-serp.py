#ТРЕУГОЛЬНИК СЕРПИНСКОГО
#1. БИБЛИОТЕКИ
import turtle
import math
t = turtle.Turtle()

#2. КОНСТАНТЫ
LEN = 100 #Длина стороны треугольника(px)
COLOR = "black" #Цвет треугольника
BACK_COLOR = "white" #Цвет фона
DEPTH = 3 #Глубина (насколько мелкими будут треугольники)
#Координаты треугольника
X = 0
Y = 0

#3. КОД. АЛГОРИТМЫ
t.screen.bgcolor(BACK_COLOR)
t.penup()
t.setpos(X, Y)
t.pendown()
t.speed(0)
t.color(COLOR)
t.begin_fill()
t.left(60)
t.forward(LEN)
t.right(120)
t.forward(LEN)
t.right(120)
t.forward(LEN)
t.end_fill()
t.left(180)
t.color(BACK_COLOR)

def triangle(x: float, y: float, l: float, dep: int):
    if dep == 0:
        return

    t.penup()
    t.setpos(x + l/2*math.cos(math.radians(60)), y + l/2*math.sin(math.radians(60)))
    t.pendown()
    t.begin_fill()
    t.forward(l/2)
    t.right(120)
    t.forward(l/2)
    t.right(120)
    t.forward(l/2)
    t.end_fill()
    t.right(120)

    triangle(x, y, l/2, dep-1)
    triangle(x + l/2*math.cos(math.radians(60)), y + l/2*math.sin(math.radians(60)), l/2, dep-1)
    triangle(x + l/2, y, l/2, dep-1)

#4. ВЫЗОВ АЛГОРИТМА И КОНЕЦ
triangle(X, Y, LEN, DEPTH)
input("PRESS ANY KEY")