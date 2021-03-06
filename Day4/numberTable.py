# Program to print number table from 1  to 10

num = int(input("Enter any number : "))

counter = 1 

while counter < 11 :
    product = num*counter
    print(num," x ", counter, " = ", product)    
    counter = counter +1
    