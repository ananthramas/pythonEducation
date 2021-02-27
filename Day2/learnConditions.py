#  18 > = Adult
#  5-17 = Child
#  >0 - 5 = Infant

your_age = int(input("Enter you age : "))

if your_age >= 18 :
 print("ADULT")
elif your_age > 5 :
  print("CHILD")
else :
  print("INFANT")
