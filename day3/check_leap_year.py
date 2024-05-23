#File:check_leap_year.py
#Description: check if a year is a leap year
#Functions used: input(), int(), print(), %, ==, !=
#Skills learned: if-else statement, boolean expressions, type conversion, arithmetic operators

print("Welcome to the leap year checker.")
year=int(input("Which year do you want to check? "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# End of file