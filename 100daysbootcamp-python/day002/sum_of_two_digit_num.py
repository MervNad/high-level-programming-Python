#File: day2.py
#Description: python data types, and string subscriting
#Functions used: len(), type(), input().
#Skills learned: string slicing, string concatenation, string interpolation, string formatting, string methods, string functions, string indexing.

two_digit_number=input("Type a two digit number: ")
print(type(two_digit_number))
print(len(two_digit_number))
first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
print(first_digit)
print(second_digit)
result=int(first_digit)+int(second_digit)
print(result)
print("The sum of the two digits is: " + str(result))
print(f"The sum of the two digits is: {result}")
print("The sum of the two digits is: {}".format(result))
print("The sum of the two digits is: %d" % result)
print("The sum of the two digits is: %s" % result)