
# Program to validate PIN

actual_pin = "007"
max_attempt = 3


attempt_counter = 0

while attempt_counter < 3 and actual_pin != input("Please enter pin - ") :  #Exit condition
    print("invaild pin... Please re enter")
    attempt_counter = attempt_counter + 1

if attempt_counter <3 :
    print("Welcome to Python world")
else :
    print(" Better Luck next time! Locked for 10 min")

   
