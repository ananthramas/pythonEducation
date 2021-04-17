# import required modules
import turtle
import time
import random

delay = 0.3
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("Arrow Control Game")
wn.bgcolor("blue")
# the width and height can be put as usdder's choice
wn.setup(width=600, height=600)
wn.tracer(0)

currentColor = 'white'

downColor = 'white'
upColor = 'yellow'

segment = turtle.Turtle()
segment.hideturtle()
segment.up()
segment.goto(-300,0)
segment.down()

ballx = -275
bally = -2

ball = turtle.Turtle()
ball.penup()
ball.hideturtle()
ball.goto(-275, -2)
ball.pendown()
ball.color('black',currentColor)
ball.begin_fill()
ball.circle(10)
ball.end_fill()

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 Lives : 3",
          align="center",
          font=("candara", 24, "bold"))


arrow = turtle.Turtle()
arrow.speed(1)
xVal = [-275, -225, -175, -125 ,-75, -25, 25, 75, 125, 175, 225, 275]

arrowX = 0

def refreshScrore(score, life):
  global pen
  pen.clear()
  pen.write("Score : {} Life : {} ".format(score, life),
            align="center",
            font=("candara", 24, "bold"))

def drawArrow():
  time.sleep(delay)
  global arrowX
  arrowX = random.choice(xVal)
  arrow.reset()
  arrow.penup()
  arrow.goto(arrowX,300)
  arrow.down()
  arrow.right(90)
  arrow.forward(250)
  
  #arrow.clear()

  
def drawSeg():
  for segCount in range(6) : 
    segment.forward(50)

    segment.left(90)
    segment.forward(50)

    segment.right(90)
    segment.forward(50)

    segment.right(90)
    segment.forward(50)

    segment.left(90)


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

  if ballx > -275 : 
    ballx  = ballx - 50
   
    if bally == 52 :
      bally  = 2
    else :
      bally  =  52

    ball.clear()
    ball.penup()
    ball.goto(ballx, bally)
    ball.pendown()
    drawBall()

def goright():
  global ballx,bally

  if ballx <= 250 : 
    ballx  = ballx + 50
  
    if bally == 52 :
      bally  = 2
    else :
      bally  = 52
    
    ball.clear()
    ball.penup()
    ball.goto(ballx, bally)
    ball.pendown()
    drawBall()

drawSeg()

wn.listen()
#wn.onkeypress(goup, "w")
#wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

lifeCount = 3
level = 0

prevEnd = -275
# Main Gameplay
while True:
    if ballx == 275 or  ballx == -275 :
      if prevEnd != ballx :
        level +=1
        refreshScrore(level,lifeCount)
        prevEnd = ballx
      
    if level == 2 :
      wn.bgcolor("green")

    if arrowX == ballx  and lifeCount > 0 :
      lifeCount -= 1
      refreshScrore(level,lifeCount)

    
    wn.update()
   
    if lifeCount > 0 :
      drawArrow()
    else :
      wn.bgcolor("red")

    time.sleep(delay)

wn.mainloop()
