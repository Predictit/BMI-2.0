
height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi = round(weight / (height ** 2))
print("Your BMI is", bmi)
if bmi < 18.5:
    print("Under the underweight")
elif 18.5 < bmi < 25:
    print("Normal weight")
elif 25 < bmi < 30:
    print("Overweight")
elif 30 < bmi < 35:
    print("Obese")
else:
    print("Clinically obese")