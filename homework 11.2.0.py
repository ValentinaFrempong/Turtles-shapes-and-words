

from turtle import *
from random import *

bck = Screen()
bck.setup(600,600)
bck.bgcolor("#114273")

speed(12421671)

colormode(255)

def randomcolor():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    color(red,green,blue)
        
def randomplace():
    penup()
    x = randint(-300,300)
    y = randint(-400,400)
    goto(x,y)
    pendown()
    
def randomheading():
    number = randint(1,360)
    setheading(number)

def drawrectangle():
    randomcolor()
    randomplace()
    hideturtle()
    length = randint(10,100)
    height = randint(10,100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

def writemyname():
    randomcolor()
    randomplace()
    style=("Comic Sans MS",30,"bold")
    write("By valentina!!!",font=style,align="center")

clear()



shape("turtle")

for draw in range(2):
    for turtles in range(30):
        randomcolor()
        randomplace()
        randomheading()
        stamp()

    clear()
    setheading(0)


    for shape in range(30):
        drawrectangle()

    clear()
    setheading(0)


    for names in range(50):
        writemyname()

    clear()

for names in range(50):
    randomheading()

    




