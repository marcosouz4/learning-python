ex_list_1 = [5, 4, 3, 2, 1]
ex_nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ex_mixed_list = [1, "Hello", True, 3.14, [1, 2, 3]]

# Print lists
print(ex_list_1)
print(ex_nested_list)
print(ex_mixed_list)

# Print list length
print(len(ex_list_1))
# 5

# contains
print(5 in ex_list_1)  # True

not_in_example = 8 not in ex_list_1  # True
print(not_in_example)

# Accessing by index
print(ex_list_1[0])  # 5

# Accessing by negative index
print(ex_list_1[-1])  # 1 (last value)

# Accessing by range
print(ex_list_1[0:3])  # [5, 4, 3]
print(ex_list_1)

# List slicing
sliced = [1, 2, 3, 4, 5]
newSlice = sliced[0:4]
print(newSlice)  # [1, 2, 3, 4]

# List slicing with step
print(sliced[0:4:2])  # [1, 3]

# List slicing with negative step
print(sliced[::-2])  # [5, 3, 1]

# Reassigning values
sliced[0] = 10
print(sliced)  # [10, 2, 3, 4, 5]
