console = {
    "Xbox": "Microsoft",
    "Playstation": "Sony",
    "Nintendo": "Nintendo",
}

# from keys
test1 = {}.fromkeys(["Xbox", "Playstation", "Nintendo"], "Console")
print(test1)
# {'Xbox': 'Console', 'Playstation': 'Console', 'Nintendo': 'Console'}

# pop
console.pop("Xbox")  # If the key is not found, it'll raise an error
print(console)
# {'Playstation': 'Sony', 'Nintendo': 'Nintendo'}

# popitem
console.popitem()  # Remove last item
print(console)
# {'Playstation': 'Sony'}

# clear
console.clear()
print(console)
# {}

# update
console.update({"Xbox": "Microsoft", "Playstation": "Sony"})
print(console)
# {'Xbox': 'Microsoft', 'Playstation': 'Sony'}

# copy
console_copy = console.copy()
console_copy["Playstation"] = "Sony updated"
print(console_copy)
# {'Xbox': 'Microsoft', 'Playstation': 'Sony', 'Nintendo': 'Nintendo'}

# set default
# console = {'Xbox': 'Microsoft', 'Playstation': 'Sony'}
console.setdefault("Xbox", "Microsoft updated")
print(console)  # {'Xbox': 'Microsoft', 'Playstation': 'Sony'}
# Because Xbox already exists, it won't update the value

# set default with default value
console.setdefault("Nintendo", "Nintendo added")
print(console)  # {'Xbox': 'Microsoft', 'Playstation': 'Sony', 'Nintendo': 'Nintendo'}
# Because Nintendo doesn't exist, it'll add it to the dictionary

# dict()
empty = dict()
print(empty)

with_values = dict(Xbox="Microsoft", Playstation="Sony", Nintendo="Nintendo")
print(with_values)
# {'Xbox': 'Microsoft', 'Playstation': 'Sony', 'Nintendo': 'Nintendo'}

# dict.fromkeys()
keys = ["Xbox", "Playstation", "Nintendo"]
values = ["Microsoft", "Sony", "Nintendo"]

with_keys = dict.fromkeys(keys, values)
print(with_keys)
