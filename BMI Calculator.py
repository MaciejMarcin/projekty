height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg "))

BMI = weight / height ** 2

BMIr = round(BMI)

if BMIr <= 18.5:
    print("You are underweight")
elif BMIr <= 25:
    print("You have a normal weight")
elif BMIr <= 30:
    print("You have overweight")
elif BMIr <= 35:
    print("You are obese")
else:
    print("You are clinically obese")

input()




