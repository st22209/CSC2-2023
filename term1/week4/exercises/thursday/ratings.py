age_ratings = {
    12: ["no"],
    13: ["R13"],
    15: ["R13"],
    16: ["R16", "R13"],
    18: ["R18", "R16", "R13"],
}
age = int(input("How old are you? "))
closest = min(age_ratings.items(), key=lambda x: abs(x[0] - age))
print(f"You can watch {', '.join(closest[1])} rated movies")

# TODO use movie api to get list of movies
