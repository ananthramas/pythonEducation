
  
import turtle 

chintu = turtle.Turtle()
chintu.shape("turtle")

def draw1():
  chintu.left(90)
  chintu.forward(50)

def draw2() :
  chintu.forward(25)
  chintu.up() # lift pen up
  chintu.backward(25) # pixels
  chintu.down()# pen down
  chintu.left(90) # 
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)

def draw3() :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.up()
  chintu.back(25)
  chintu.down()
  chintu.right(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)

def draw4() :
  chintu.left(90)
  chintu.up()
  chintu.forward(50)
  chintu.down()
  chintu.backward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.backward(13)
  chintu.left(90)
  chintu.forward(13)
  chintu.backward(39)

def draw5() :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)

def draw6() :
  chintu.left(90)
  chintu.up()
  chintu.forward(25)
  chintu.right(90)
  chintu.down()
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(25)
  chintu.right(90)
  chintu.forward(50)
  chintu.right(90)
  chintu.forward(25)

def draw7() :
  chintu.up()
  chintu.forward(25)
  chintu.down()
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90   )
  chintu.forward(25) 

def draw8() :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.up()
  chintu.back(25)
  chintu.down()
  chintu.left(90)
  chintu.forward(25)

def draw9():
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(25)

def draw0() :
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)
  chintu.left(90)
  chintu.forward(25)
  chintu.left(90)
  chintu.forward(50)

xCor = chintu.xcor();
yCor= chintu.ycor();



while True: 
  
  chintu.hideturtle()
  number = input("Enter number to be displayed - ")
  chintu.reset() # wipe off screen content
  chintu.showturtle()
  
  xCor =0  # initial x location

  if number=="007" :   # condition exit loop
    break
  
  for num  in number :  # get single digit and draw it
    num = int(num)
    if num == 1 :
      draw1()
    elif num == 2 :
      draw2()
    elif num== 3 :
      draw3()
    elif num == 4 :
      draw4()
    elif num == 5 :
      draw5()
    elif num== 6 :
      draw6()
    elif num == 7 :
      draw7()
    elif num == 8 :
      draw8()
    elif num == 9 :
      draw9()
    elif num == 0 :
      draw0()
    else :
      print(num ,"not supported ")
    if  num == 1 : 
     xCor = xCor + 10
    else :
      xCor = xCor + 30
    
    chintu.up()  # while resting psotion lifft pen i.e don't draw
    #chintu.home() # start from intial location
    chintu.goto(xCor, yCor) # start drawing
    chintu.down()  

    chintu.left(360-chintu.heading())
   
