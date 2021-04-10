import turtle
import random

chintu = turtle.Turtle()
chintu.speed(0)
colours = ["red", "yellow", "blue", "purple", "green", "gold", "aqua"]

length = 500
angle = 91
circle_size = 10

for side in range(length):
  #print side
  colour = random.choices(colours)

  chintu.color(colour,colour)
    
  #chintu.pencolor(colour)
  #chintu.fillcolor(colour)
  
  chintu.penup()
  chintu.forward(side)
  chintu.pendown()
  chintu.left(angle)
  chintu.begin_fill()
  chintu.circle(circle_size)
  chintu.end_fill()


turtle.exitonclick()
