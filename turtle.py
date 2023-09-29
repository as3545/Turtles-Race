import turtle
from turtle import *
import random
from random import *
penup()
goto(-140,140)

screen=turtle.Screen()
screen.bgcolor('black')
for i in range(15):
    speed(100)
    color('red')
    write(i)
    right(90)
    color('green')
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

t1=Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-160,100)
t1.pendown()

t2=Turtle()
t2.color('pink')
t2.shape('turtle')
t2.penup()
t2.goto(-160,80)
t2.pendown()

t3=Turtle()
t3.color('orange')
t3.shape('turtle')
t3.penup()
t3.goto(-160,60)
t3.pendown()

for chance in range(100):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    
    
turtle.done()
