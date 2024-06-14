target = int(input())
total_even_sum = 0
for num in range(1, target+1):
    if (num % 2 == 0):
        total_even_sum += num 
print(total_even_sum)