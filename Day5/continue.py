#Pizza
#Burger
#Fries - > Peri Peri mala
#       > normal


order ="" #initialization 

print("-----Crunch n Munch-------")
while order!="exit" :
    order = input("Enter your order - ") 

    if order == "pizza" or order == "burger" :
            print ("Your order is "+order+"  Preparation in progress...")
            continue

    if order == "fries" :
        withPeriperi = input("fries with Peri Peri Masala y/n -")
     
        if withPeriperi == "y" :
            order = "Fries with Peri Peri"
        print ("Your order is "+order+"  Preparation in progress...")
    else :
        print ("Sorry we don't serve "+order)

    
  