ex_list_1 = [
    "pluto",
    "mars",
    "earth",
    "venus",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "mercury",
]

del ex_list_1[0]  # index
print(ex_list_1)

# Remove method
ex_list_1.remove("earth")  # It'll remove only the first occurrence
print(ex_list_1)

# Add to list
ex_list_1.append("XP")
ex_list_1.append("fast")
print(ex_list_1)  # [5, 4, 3, 2, 1, 0, 1]

# Insert
ex_list_1.insert(0, "furious")
print(ex_list_1)

ex_list_1.sort()
print(ex_list_1)  # It'll be sorted

ex_list_1.sort(reverse=True)
print(ex_list_1)  # It'll be sorted in reverse

# CANNOT USE SORT IN MIXED LISTS
# But False is 0 and True is 1, so we can use it to sort lists mixed with ints and booleans

# Uppercase will be before lowercase
alpha_list = ["a", "b", "c", "A", "B", "C"]
alpha_list.sort()
print(alpha_list)

# Sort by lowercase
alpha_list.sort(key=str.lower)
print(alpha_list)

# Get Index
print(alpha_list.index("a"))  # It'll return the index of first occurence
# Or it'll raise an error

# Pop
alpha_list.pop()
print(alpha_list)

# Pop return the item removed, so we can assign it to a variable
removed_item = alpha_list.pop()
print(removed_item)

# Strings vs Lists
# Strings are immutable, lists are mutable
# I cant change a character in a string, but I can change a value in a list
