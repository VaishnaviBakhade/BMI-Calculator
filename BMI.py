weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

BMI = weight / height ** 2

if BMI < 18.5:
    print("Under weight")

elif BMI < 25:
    print("Healthy weight")

else:
    print("Over weight")