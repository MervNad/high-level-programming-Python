#File: tip_calulator.py
#Description: calculate the tip amount and the total bill amount after adding the tip
#Functions used: input(), float(), print(), round()
#Skills learned: string interpolation, string formatting, string concatenation, string methods, string functions, floating point arithmetic.

print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage=float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_amount=total_bill*(tip_percentage/100)
total_bill_with_tip=total_bill+tip_amount
bill_per_person=round(total_bill_with_tip/people, 2)
print(f"Each person should pay: ${bill_per_person}")
# print("Each person should pay: $" + str(bill_per_person))
# print(f"Each person should pay: {bill_per_person}")
# print("Each person should pay: {}".format(bill_per_person))
# print("Each person should pay: %d" % bill_per_person)
# print("Each person should pay: %s" % bill_per_person)
# print("Each person should pay: $" + str(bill_per_person))

