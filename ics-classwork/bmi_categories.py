height = float(input("Your height in m: "))
weight = float(input("Your weight in kg: "))
answer = weight / (height**2)

print(f"Your BMI is {answer}.")
if answer < 15:
    print("BMI Category: Very Severely Underweight")
if answer >= 15 and answer <= 16:
    print("BMI Category: Severely Underweight")
if answer >= 16.01 and answer <= 18.4:
    print("BMI Category: Underweight")
if answer >= 18.5 and answer <= 24.9:
    print("BMI Category: Normal Weight")
if answer >= 25 and answer <= 29.9:
    print("BMI Category: Overweight")
if answer >= 30 and answer <= 34.9:
    print("BMI Category: Moderately Obese")
if answer >= 35 and answer <= 39.9:
    print("BMI Category: Severely Obese")
if answer >= 40:
    print("BMI Category: Morbidly Obese")