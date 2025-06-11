# similar to list, but immutable

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5, 4, 3, 2, 1)
print(my_tuple)  # (1, 2, 3, 4, 5, 4, 3, 2, 1)

# Creating with a tuple function
# my_tuple = tuple([1, 2, 3, 4, 5])
# print(my_tuple)  # (1, 2, 3, 4, 5)

# my_tuple = tuple("Hello")
# print(my_tuple)  # ('H', 'e', 'l', 'l', 'o')

# # Creating a tuple with one element
# my_tuple = (1,)
# print(my_tuple)

# Accessing values
print(my_tuple[0])  # 1

# Slicing
print(my_tuple[0:3])  # (1, 2, 3)

# Negative indexing
print(my_tuple[-1])  # 1

# Reassigning values
# my_tuple[0] = 10
# print(my_tuple)  # (1, 2, 3, 4, 5, 4, 3, 2, 1)
# Tuples are immutable, so this will raise an error

print("--------------------------------")

# Sizeof
print((1, 2, 3).__sizeof__())  # 48 bytes
print([1, 2, 3].__sizeof__())  # 72 bytes
# Tuples are more efficient than lists

print("-------------------------------- For:")

# For loop
for i in my_tuple:
    print(i)

print("-------------------------------- For range:")

# For loop with index
for i in range(len(my_tuple)):
    print(my_tuple[i])

print("-------------------------------- While:")

# While loop
count = 0
while count < len(my_tuple):
    print(my_tuple[count])
    count += 1

print("--------------------------------")

# Slicing with step
print("Slicing with step:")
print(my_tuple[0:5:2])  # (1, 3, 5)

# Slicing with negative step
print("Slicing with negative step:")
print(my_tuple[::-1])  # (1, 2, 3, 4, 5, 4, 3, 2, 1)

# Slicing with negative step and start
print("Slicing with negative step and start:")
print(my_tuple[::-1][0:5])  # (1, 2, 3, 4, 5)

print("original:")
print(my_tuple)


# METHODS
print("Methods:")
print(my_tuple.count(1))  # 2
print(my_tuple.index(5))  # 4, return first occurrence or an error

# Tuple nested
new_tuple = (1, 2, 3, (4, 5, 6))
print(new_tuple)
