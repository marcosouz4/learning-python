ex_1 = "This is a string"
ex_2 = "This is also a string"

# Access by index
ex_8 = "orange"
print(ex_8[2])  # "o"
print("orange"[2])  # "o"

print("----")

# String slicing
ex_9 = "tomato"
print(ex_9[:3])  # "tom"
print(ex_9[3:5])  # "at"
print("tomato"[3:])  # "ato"
print(ex_9)  # No changes

# Concat
ex10 = ex_1 + " - " + ex_2
print(ex10)

# String multiplication
ex11 = "Hello" * 3
print(ex11)

# String methods
ex12 = "Hello"
print(ex12.upper())

# convert to string
ex_01 = "This is a string"
ex_02 = str(1)
ex_03 = str(False)

print(type(ex_01))
print(type(ex_02))
print(type(ex_03))

# Escape
print("This\tis\ta\tlot\tof\tspaces")

print("line one\nline two")

# To Upper
all_low = "lorem ipsum dolor sit amet"
print(all_low.upper())

# To Lower
all_up = "LOREM IPSUM DOLOR SIT AMET"
print(all_up.lower())

# Capitalize
print(all_low.capitalize())

# Is all Upper?
print(all_up.isupper())

# Is all Lower?
print(all_low.islower())

# isalpha() = only letters
# isalphanum() = letters and numbers
# isdecimal() = only NUMBERS (no dots)
# isspace() = only spaces
# istitle() = only title case

# startswith("this") / Checks if the string starts with "this"
# endswith("this") / Checks if the string ends with "this"

# strip() / Removes whitespace from the beginning and end of the string
# lstrip() / Removes whitespace from the left side of the string
# rstrip() / Removes whitespace from the right side of the string
# We can pass a parameter to strip() to remove a specific character
# Example: .strip("H") will remove the H from the beginning and end of the string
print("  Hello  ".strip())


# Joins
print(
    " - ".join(["Hello", "World", ".", "How are you?"])
)  # It'll insert a - between each item
# Hello - World - . - How are you?


# Split
print("Hello World How are you?".split("o"))
# ['Hell', ' W', 'rld H', 'w are y', 'u?']

# Split by space
print("Hello World How are you?".split(" "))
# ['Hello', 'World', 'How', 'are', 'you?']

# Index
print("Hello World How are you?".index("o"))
# 4

# Count
print("Hello World How are you?".count("o"))
# 4

# Replace
print("Hello World How are you?".replace("o", "a"))
# Hella Warld Haw are yau?


# RJust / LJust - Same as padLeft / padRight in JS
print("Hello".rjust(10))
#     Hello
print("Hello".ljust(10, "."))
# Hello
print("Hello".center(99, "-"))
# -----------------------------Hello-----------------------------
