#File: life_in_weeks.py
#description: calculate the number of days, weeks, and months left in your life if you live until 90 years old.
#functions used: input(), int(), print()
#skills learned: integer division, modulus operator, f-string, string interpolation, string formatting, string concatenation, string methods, string functions.

age=input("What is your current age? ")
age_int=int(age)
years_remaining=90-age_int
months_remaining=years_remaining*12
weeks_remaining=years_remaining*52
days_remaining=years_remaining*365
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
# print("You have " + str(days_remaining) + " days, " + str(weeks_remaining) + " weeks, and " + str(months_remaining) + " months left.")
# print("You have {} days, {} weeks, and {} months left.".format(days_remaining, weeks_remaining, months_remaining))
# print("You have %d days, %d weeks, and %d months left." % (days_remaining, weeks_remaining, months_remaining))
# print("You have %s days, %s weeks, and %s months left." % (days_remaining, weeks_remaining, months_remaining))
# print("You have " + str(days_remaining) + " days, " + str(weeks_remaining) + " weeks, and " + str(months_remaining) + " months left.")
