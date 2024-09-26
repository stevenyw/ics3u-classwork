height = float(input("Height in inches: "))
weight = float(input("Weight in pounds: "))
newheight = 0.0254*height
newweight = 0.453592*weight

bmi = newweight / (newheight**2)
newbmi = (round(bmi, 6))

print(f"The BMI is {newbmi}")
# I can't figure out how they got 23.625289 lol