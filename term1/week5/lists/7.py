list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print("\n".join([f"{i} {j}" for i, j in zip(list1, list2[::-1])]))

list1 = [1, 2, 3, 4]
list3 = [100, 200, 300, 400]

for i, value in enumerate(list1):
    print(value, list3[int(f"-{i + 1}")])
