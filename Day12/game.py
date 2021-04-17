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

currentColor = 'white'

downColor = 'white'
upColor = 'yellow'


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
ball.color('black',currentColor)
ball.begin_fill()
ball.circle(10)
ball.end_fill()


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


def drawBall() :
  global currentColor
  
  if currentColor == 'white':
    currentColor = 'yellow'
  elif currentColor == 'yellow' : 
    currentColor = 'white'

  ball.color('black',currentColor)
  ball.begin_fill()
  ball.circle(10)
  ball.end_fill()

def goup():
  global bally
  bally  = bally + 10
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)


def godown():
  global bally
  bally  = bally - 10
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  ball.circle(10)

def goleft():
  global ballx,bally

  ballx  = ballx - 50
  
  if bally < 45 :
    bally  = bally + 50
  
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  drawBall()

def goright():
  global ballx,bally

  ballx  = ballx + 50
  
  if bally < 45 :
    bally  = bally + 50
  
  ball.clear()
  ball.penup()
  ball.goto(ballx, bally)
  ball.pendown()
  drawBall()

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
