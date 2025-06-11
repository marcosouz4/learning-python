import copy

ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9

ex_10.append(6)

print(ex_9)
print(ex_10)

# Both lists are the same, because ex_10 is a reference to ex_9
# If I change ex_10, ex_9 will also change
# If I change ex_9, ex_10 will also change

print("--------------------------------")
# How to copy a list?
ex_11 = copy.deepcopy(ex_9)

ex_11.append(7)

print(ex_9)
print(ex_11)

# Now ex_11 is a copy of ex_9, so if I change ex_11, ex_9 will not change
a = (
    1213123
    + 213231213
    + 123123231
    + 21332123213
    + 123321231
    + 1231234213
    + 2132131231
    + 123123
    + 21321
    + 4534
)

# or use \ to break the line
