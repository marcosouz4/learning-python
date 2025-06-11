# While loop

counter = 0
while counter < 3:
    print("Smth")
    counter += 1

print("----------")

for i in range(3):
    print("Smth")

print("----------")

int_1 = 1
int_2 = 10
for i in range(int_1, int_2):
    print(i)

print("----------")

# Start, stop, step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9, last param is step
    print(i)

print("----------")


word = "house"
for letter in word:
    print(letter)
