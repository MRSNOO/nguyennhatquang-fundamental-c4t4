inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
inventory["pocket"] = ["seashell", "strangeberry", "lint"]
del inventory["backpack"][1]
inventory["gold"] = [500]
inventory["gold"].append(50)
print(inventory,end="\t")


