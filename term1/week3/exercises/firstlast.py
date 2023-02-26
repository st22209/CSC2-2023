name = input("What is your full name? ")
fname, lname = name.split()

idx = name.find(" ")
fname = name[:idx]
lname = name[idx + 1 :]

print(f"Firstname: {fname}\nLastname: {lname}")
