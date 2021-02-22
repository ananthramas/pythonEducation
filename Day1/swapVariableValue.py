#Progrm to swap content of shriyans_bottle and tanvi_bottle

shriyans_bottle = "Apple juice"
tanvi_bottle = "Lemon juice"

print("---Content in variables---")

print("shriyans_bottle - "+shriyans_bottle)
print("tanvi_bottle - "+tanvi_bottle)

#Use temp variable to hold the content
temp_bottle = shriyans_bottle 

shriyans_bottle = tanvi_bottle 

tanvi_bottle = temp_bottle


print("---Content after exchange---")

print("shriyans_bottle - "+shriyans_bottle)
print("tanvi_bottle - "+tanvi_bottle)