console = {
    "Xbox": "Microsoft",
    "Playstation": "Sony",
    "Nintendo": "Nintendo",
}

print(console)

# Accessing values
print(console["Xbox"])

# Adding values
console["Atari"] = "Atari"
print(console)

# Updating values
console["Xbox"] = "Microsoft!"
print(console)

# Removing values
del console["Xbox"]
print(console)

# Keys
print(console.keys())
# dict_keys(['Playstation', 'Nintendo', 'Atari'])
# I can iterate over keys using for (for key in console.keys())

# Values
print(console.values())
# dict_values(['Sony', 'Nintendo', 'Atari'])
# I can iterate over values using for (for value in console.values())
# We can convert the return to a list
print(list(console.values()))

# Items
print(console.items())
# dict_items([("Playstation", "Sony"), ("Nintendo", "Nintendo"), ("Atari", "Atari")])
# I can iterate over items using for (for k, v in console.items())

# Check if key exists
print("Xbox" in console)
# False

# Check if value exists
print("Sony" in console.values())
# True

# Get value with default
print(console.get("Xbox", "Unknown"))

# Dictionary are also passed by reference
