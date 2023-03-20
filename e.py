import os
import time

# shopping list!!!
shopping_list = []
while (
    mode := input(
        "What would you like to do?\na: Add item to list\nr: Remove item from list\nc: Clear all elements from list\ns: sort all items\nq: quit the program\n> "
    )
) != "q":
    match mode:
        case "a":
            item = input("What would you like to add to the list? ")
            shopping_list.append(item)
            print("Item added")
        case "r":
            item = input("What would you like remove from the list? ")
            shopping_list.remove(item)
            print("Item removed")
        case "c":
            shopping_list.clear()
            print("List Cleared")
        case "s":
            shopping_list = sorted(shopping_list)
    print("List Summary:\n", "\n".join(shopping_list))
    time.sleep(0.5)
    os.system("clear")
