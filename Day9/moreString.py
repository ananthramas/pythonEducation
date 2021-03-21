
greeting = "Hello "

nameStr = input("Please enter name : ")

# concatenation of string
print(greeting + nameStr)

#Extracting all chars
for charStr in nameStr:
    print(charStr)

# index starts on 0
print("4th char : ", nameStr[3])

#Sub string / slicing
print("3 to 5t char : ", nameStr[2:5])

print("Length of string ", len(nameStr))

# -
print("last char : ", nameStr[-1])

print("reverse : ", nameStr[::-1])

isItIn = "Python" not in "Hello Python"

print(isItIn)
