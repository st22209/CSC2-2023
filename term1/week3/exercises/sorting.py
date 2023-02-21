num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

sorted_ints = sorted([num1, num2, num3])

print(f'In increasing order: {", ".join(map(str, sorted_ints))}')

# print(f'In increasing order: {", ".join(map(str, sorted([int(input("Enter first number:")), int(input("Enter second number:")), int(input("Enter third number:"))])))}')
