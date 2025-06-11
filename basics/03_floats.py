print(1.23 + 2.80)  # 4.029999999999999

# Why do expressions that involve floats produce inaccurate results?

# Python is built on C and C uses approximate values to represent floats
# This is why 1.23 + 2.80 is not exactly 4.03
# And the 4.03 is not exactly 4.03

# To fix this, we can use two ways

# Use integer values at all
ex2 = (123 + 280) / 100
print(ex2)

# Use round function
ex3 = round(1.23 + 2.80, 2)
print(ex3)

# print(round(1.23 + 2.80, 2))  # 4.03

# # We can also use the decimal module
# from decimal import Decimal

# print(Decimal("1.23") + Decimal("2.80"))  # 4.03
