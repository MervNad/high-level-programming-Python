#File:odd_even.py
#Description: check if a number is odd or even
#Functions used: input(), int(), print(), %
#Skills learned: modulus operator, if-else statement, boolean expressions, type conversion

print("Welcome to the odd-even number checker.")
number=int(input("Which number do you want to check? "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")
