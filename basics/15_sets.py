# Sets are unordered collections of unique elements

set_1 = {9, 8, 7, 6, 5, 4, 3, 2, 1}
print(set_1)

# Creating with a set function
set_2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(set_2)

# Creating with a set comprehension
set_3 = {i for i in range(1, 10)}
print(set_3)

comp_1 = {even + 2 for even in range(2, 11, 2)}
print("Comprehension:")
print(comp_1)  # {4, 6, 8, 10, 12}

# Creating with range
set_4 = set(range(1, 10, 2))
print(set_4)  # {1, 3, 5, 7, 9}

# Creating with a string
set_5 = set("Hello")
print(set_5)

# In
print("H" in set_5)  # True

print("-----------")
set_5 = {"H", "e", "l", "o"}
print(set_5)

# add
set_5.add("!")
print(set_5)  # {'H', 'e', 'l', 'o', '!'}

# update
set_5.update(["Hello", "World"])
print(set_5)  # {'H', 'e', 'l', 'o', '!', 'Hello', 'World'}

# remove
set_5.remove("!")  # remove raises an error if the element is not found
print(set_5)  # {'H', 'e', 'l', 'o', 'Hello', 'World'}

# discard
set_5.discard("!")  # discard doesn't raise an error if the element is not found
print(set_5)  # {'H', 'e', 'l', 'o', 'Hello', 'World'}

# pop
set_5.pop()
print(set_5)  # {'e', 'l', 'o', 'Hello', 'World'}

# intersection
set_6 = {1, 2, 3, 4, 5}
set_7 = {4, 5, 6, 7, 8}
print(set_6.intersection(set_7))  # {4, 5}
# or:
print(set_6 & set_7)  # {4, 5}

# union
print(set_6.union(set_7))  # {1, 2, 3, 4, 5, 6, 7, 8}
# or
print(set_6 | set_7)  # {1, 2, 3, 4, 5, 6, 7, 8}

# difference
print(set_6.difference(set_7))  # {1, 2, 3}
# or
print(set_6 - set_7)  # {1, 2, 3}

# copy
set_8 = set_6.copy()
print(set_8)

# clear
set_8.clear()
print(set_8)
print(set_6)
