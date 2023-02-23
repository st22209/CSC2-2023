import random

foods = {
    "apple": "fruit",
    "grape": "fruit",
    "bacon": "meat",
    "steak": "meat",
    "worm": "not food",
    "dirt": "not food",
}
food, cat = random.choice(list(foods.items()))
print(f"Food Picked {food}. Food Category: {cat}")