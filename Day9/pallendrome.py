

print("---Pallendrome check---")
inputStr = input("Enter string ")

revserStr = inputStr[::-1]

if inputStr == revserStr :
  print (inputStr, "is a pallendrome!")
else :
  print (inputStr, "is not a pallendrome!")


