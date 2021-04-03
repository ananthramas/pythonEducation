import turtle 
import time

chintu = turtle.Turtle()
chintu.shape("turtle")

chintu.forward(200)
chintu.left(90)
chintu.forward(50)


chintu.right(90)

chintu.up()
chintu.goto(0,10)
chintu.down()
  
chintu.fillcolor("red")

for x in range(10) :
  stampId = chintu.stamp()
  chintu.up()
  chintu.forward(20)
  chintu.down()
  chintu.clearstamp(stampId)
  time.sleep(1)


chintu.shape("classic")

#time.sleep(5)


turtle.exitonclick()