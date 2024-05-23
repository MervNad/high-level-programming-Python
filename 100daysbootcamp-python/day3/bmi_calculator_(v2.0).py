#File:bmi_calculator_(v2.0).py
#Description: calculate BMI and give advice
#Functions used: input(), float(), print(), /, **, >=, <=
#Skills learned: if-else statement, boolean expressions, type conversion, arithmetic operators

print("Welcome to the BMI calculator.")
weight=float(input("What is your weight in kg? "))
height=float(input("What is your height in m? "))
bmi=weight/height**2
if bmi<18.5:
    print(f"Your BMI is: {bmi}, You are underweight.")
elif bmi<25:
    print(f"Your BMI is: {bmi}, You have normal weight.")
elif bmi<30:
    print(f"Your BMI is: {bmi}, You are slightly overweight.")
elif bmi<35:
    print(f"Your BMI is: {bmi}, You have obese.")
else:
    print(f"Your BMI is: {bmi}, You are clinically obese.")
# End of file