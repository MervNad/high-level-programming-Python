# BMI formula: weight(kg) / height(m)^2
# 1. Prompt the user to enter their weight in kg
# 2. Prompt the user to enter their height in meters
# 3. Calculate the BMI
# 4. Print the BMI
# 5. Print the BMI with a message
# 6. Print the BMI with a message using string interpolation
# 7. Print the BMI with a message using string formatting
# 8. Print the BMI with a message using string concatenation
# 9. Print the BMI with a message using string interpolation and f-string
# 10. Print the BMI with a message using string formatting and % operator
# 11. Print the BMI with a message using string formatting and .format() method
# 12. Print the BMI with a message using string concatenation and str() function
# 13. Print the BMI with a message using string concatenation and + operator

weight=input("Enter your weight in kg: ")
height=input("Enter your height in meters: ")
bmi=float(weight)/float(height)**2
bmi_int=int(bmi) # this line calculates the integer part of the BMI
print(bmi_int) # this line prints the integer part of the BMI
print(bmi)
#print("Your BMI is: " + str(bmi))
#print(f"Your BMI is: {bmi}")
#print("Your BMI is: {}".format(bmi))
print("Your BMI is: %d" % bmi)
#print("Your BMI is: %s" % bmi)
#print("Your BMI is: " + str(bmi))
#print(f"Your BMI is: {bmi}")
#print("Your BMI is: {}".format(bmi))
print("Your BMI is: %d" % bmi)
#print("Your BMI is: %s" % bmi)
#print("Your BMI is: " + str(bmi))
