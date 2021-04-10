# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Arrow Control Game")
wn.bgcolor("blue")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

arrow = turtle.Turtle()
arrow.up()
arrow.goto(-300,0)
arrow.down()

ballx = -300
bally = -5

ball = turtle.Turtle()
ball.penup()
ball.hideturtle()
ball.goto(-290, 5)
ball.pendown()
ball.circle(10)


def drawSeg():
  for segCount in range(6) : 
    arrow.forward(50)

    arrow.left(90)
    arrow.forward(50)


    arrow.right(90)
    arrow.forward(50)


    arrow.right(90)
    arrow.forward(50)

    arrow.left(90)



def goup():
  global bally
  bally  = bally + 50
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)

def godown():
  global bally
  bally  = bally - 50
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)

def goleft():
  global ballx
  ballx  = ballx - 50
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)

def goright():
  global ballx
  ballx  = ballx + 50
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)

drawSeg()

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

# Main Gameplay
while True:
    wn.update()
    time.sleep(delay)

wn.mainloop()
