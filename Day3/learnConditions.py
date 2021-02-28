#  18 > = Adult
#  5-17 = Child
#  >0 - 5 = Infant

your_age = input("Enter you age : ")
your_age = int(your_age)

if your_age >= 18 :
  print("ADULT")
elif your_age > 5 and your_age < 17 :
  print("CHILD")
else :
  print("INFANT")
