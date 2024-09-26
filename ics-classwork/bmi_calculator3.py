height = float(input("Height in feet: "))
height2 = float(input("Height in inches: "))
weight = float(input("Weight in pounds: "))
height3 = height*12
newheight3 = height2 + height3
newheight2 = 0.0254*newheight3
newweight = 0.453592*weight

bmi = newweight / (newheight2**2)
newbmi = (round(bmi, 6))

print(f"The BMI is {newbmi}")
# I can't figure out how they got 23.625289 lol