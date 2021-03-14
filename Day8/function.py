
  
import turtle 

chintu = turtle.Turtle()
#chintu.shape("turtle")

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
  chintu.forward(25)
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


number = int(input("Enter number to be displayed - "));

if number == 1 :
  draw1()
elif number == 2 :
  draw2()
elif number == 3 :
  draw3()
elif number == 4 :
  draw4()
elif number == 5 :
  draw5()
elif number == 6 :
  draw6()
elif number == 7 :
  draw7()
elif number == 8 :
  draw8()
elif number == 9 :
  draw9()
elif number == 0 :
  draw0()
else :
  print(number ,"not supported ")

