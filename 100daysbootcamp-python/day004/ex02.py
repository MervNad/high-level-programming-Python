import random

names = ["Merveilles", "Jenny", "Urbain", "Hilda", "Issacar"]
print(names)

num_items = len(names)
print(num_items)

random_choice = random.randint(0, num_items - 1)
print(names[random_choice] + " " + "is going to pay the bill")