# import required modules
import turtle
import time
import random

delay = 0.3
score = 0
high_score = 0

lifeCount = 3
score = 0


initialBallX = -275
initialBallY = -2

prevEnd = initialBallX

ballX = initialBallX
ballY = initialBallY
arrowX = 0

currentColor = 'white'
downColor = 'white'
upColor = 'yellow'

# Creating a window screen
wn = turtle.Screen()
wn.title("Arrow Control Game")
wn.bgcolor("green")

# the width and height can be put as usdder's choice
wn.setup(width=600, height=600)
wn.tracer(0)

segment = turtle.Turtle()
segment.hideturtle()
segment.up()
segment.goto(-300,0)
segment.down()

#This is to create ball
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
possibleBallxVal = [-275, -225, -175, -125 ,-75, -25, 25, 75, 125, 175, 225, 275]



def refreshScore(score, life):
  global pen
  pen.clear()
  pen.goto(0, 250)
  pen.write("Score : {} Life : {} ".format(score, life),
            align="center",
            font=("candara", 24, "bold"))

def drawArrow():
  time.sleep(delay)
  global arrowX
  arrowX = random.choice(possibleBallxVal)
  arrow.reset()
  arrow.penup()
  arrow.goto(arrowX,300)
  arrow.down()
  arrow.right(90)
  arrow.forward(250)
  
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

def goleft():
  
  global ballX,ballY

  if ballX > -275 : 
    ballX  = ballX - 50
   
    if ballY == 52 :
      ballY  = 2
    else :
      ballY  =  52

    ball.clear()
    ball.penup()
    ball.goto(ballX, ballY)
    ball.pendown()
    drawBall()

def goright():
  global ballX,ballY

  if ballX <= 250 : 
    ballX  = ballX + 50
  
    if ballY == 52 :
      ballY  = 2
    else :
      ballY  = 52
    
    ball.clear()
    ball.penup()
    ball.goto(ballX, ballY)
    ball.pendown()
    drawBall()

def resetGame() :
  global ballX, ballY, lifeCount, score, pen
  ballX = initialBallX
  ballY = initialBallY
  lifeCount = 3
  score = 0
  wn.bgcolor("green")
  pen.clear()
  pen.write("Score : 0 Lives : 3",
          align="center",
          font=("candara", 24, "bold"))


drawSeg()

wn.listen()
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(resetGame, "y")

# Main Gameplay
while True:
    if ballX == 275 or  ballX == -275 :
      if prevEnd != ballX :
        score +=1
        refreshScore(score,lifeCount)
        prevEnd = ballX
      
    if arrowX == ballX  and lifeCount > 0 :
      lifeCount -= 1
      refreshScore(score,lifeCount)

    
    wn.update()
   
    if lifeCount > 0 :
      drawArrow()
    else :
      wn.bgcolor("red")
      pen.goto(0, 200)
      pen.write("Wanna play once more y/n",
          align="center",
          font=("candara", 24, "bold"))


    time.sleep(delay)

wn.mainloop()
