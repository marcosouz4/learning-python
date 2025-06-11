name = input("Tell me ur name:")
print("Your name is " + name)
# print(f"Hello {name}")

fav_num = input("What is your favorite number?")
print(fav_num + " is a great number!")
print(type(fav_num))  # String

user_int = int(
    input("Fav number:")
)  # It'll throw an error if the input is not an integer
print(user_int)
print(type(user_int))  # Integer

user_float = float(input("Enter a float:"))
print(user_float)
print(type(user_float))  # Float

user_bool = bool(input("Enter a boolean:"))
print(user_bool)
print(type(user_bool))  # Boolean
