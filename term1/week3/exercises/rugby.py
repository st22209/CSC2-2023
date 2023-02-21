name = input("Team name?")
tries = int(input("How many tries did you score?")) * 5
conv = int(input("How many conversions did you score?")) * 2
pen = int(input("How many penalties did you score?")) * 3

print(f"The {name} scored {tries+conv+pen} points today")

# print(f'The {input("Team name? ")} scored {(int(input("How many tries did you score?")) * 5)+(int(input("How many conversions did you score?")) * 2)+(int(input("How many penalties did you score?")) * 3)} points today')
