def prints_four():
    print("four")


prints_four()
print("----------")


def function_with_params(param1, param2):
    print("Param1: " + param1)
    print("Param2: " + param2)


function_with_params("Hello", "World")
print("----------")


def function_with_default_params(param1, param2="World"):
    print("Param1: " + param1)
    print("Param2: " + param2)


function_with_default_params("Hello")
print("----------")


def function_with_return(param1, param2):
    return param1 + param2


output = function_with_return(2, 5)
print(output)
print("----------")
