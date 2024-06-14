#File: love_compatibility_test.py
#Description: calculate the love compatibility between two people
#Functions used: input(), print(), ==, +, %
#Skills learned: if-else statement, boolean expressions, type conversion, arithmetic operators

print("Welcome to the Love Compatibility Test.")
name1 = input("What is your name?: ")
name2 = input("What is your partner's name?: ")
combined_name = name1 + " " + name2
print(f"Your combined name is {combined_name}.")
lower_name = combined_name.lower()
print(f"Your combined name in lowercase is {lower_name}.")
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
total_true = t + r + u + e
total_love = l + o + v + e
love_score = int(str(total_true) + str(total_love))
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")
# End of file