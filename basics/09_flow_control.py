# Comparison operators
# ==
# !=
# >
# <
# >=
# <=

# Logical operators
# and
# or
# not

# If statement
ex_1 = int(input("Enter a number: "))

if ex_1 > 5:
    print("Clayton")

    if ex_1 >= 10:
        print("Clayton is 10!")
elif ex_1 == 5:
    print("Clayton it's in average")
else:
    print("Not Clayton")


# Truthy and Falsy values
str_1 = ""  # Falsy
str_2 = "Hello"  # Truthy
int_1 = 0  # Falsy
int_2 = 1  # Truthy
