list1 = ["M", "na", "i", "Ke", "too", "long", "rrrrrr"]
list2 = ["y", "me", "s", "lly"]
shorter = min([len(list1), len(list2)])
list3 = [i + j for i, j in list(zip(list1, list2))] + list1[shorter:]+list2[shorter:]
print(" ".join(list3))