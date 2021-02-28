principalVal = int(input("Enter principal in $ - "))

timeVal = float(input("Enter no. of years - "))

rateVal = float(input("Enter rate of interest % - "))
# SI = PTR/100 
simpleInterestVal = (principalVal* timeVal * rateVal)/100

print("Simple interest would be - $",simpleInterestVal )

amount = principalVal + simpleInterestVal

print("Final amount would be  - $",amount )
