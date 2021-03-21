import turtle 
chintu = turtle.Turtle()
#chintu.shape("turtle")


#chintu.color()

colorList = ["blue", "yellow", "green", "red",]


for x in range(15) :
  chintu.begin_fill()

  chintu.color("black",colorList[x%4])

  #chintu.stamp()


  #chintu.up()
  chintu.forward(25)
  chintu.left(25)
  #chintu.down()
  
  chintu.circle(25)
  chintu.end_fill()