height = float(input(" whats your height in cm "))
weight = int(input(" whats your weight "))

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight ")
elif bmi <25:
    print(f"your BMI is  {bmi}, and you are normal weight")
elif bmi < 30:
    print(f"your BMI is {bmi}, and you are slightly overweight")
else:
    print(f"you are overweight")