dict1 = {
    "Item1": 1,
    "Item2": 2
}

dict2 = dict1.copy()

dict2["Item1"] = 7

print(dict1["Item1"])
print(dict2["Item1"])