target = int(input("Enter a positive whole number: "))
for num in range(1, target + 1):
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 5 == 0):
        print("Buzz")
    elif(num % 3 == 0):
        print("Fizz")
    else:
        print(num)