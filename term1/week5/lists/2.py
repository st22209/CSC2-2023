import random

numbers = [random.randint(1, 100) for _ in range(10)]
smallest = 101
largest = 0
total = 0
for num in numbers:
    if num < smallest:
        smallest = num
    if num >  largest:
        largest = num
    total  += num

print(total, smallest, largest)
# better way
print(sum(numbers), min(numbers), max(numbers))
