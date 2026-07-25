

rows = 5
for count in range(rows):
    for _ in range(rows - count - 2):
        print(" ", end="")

    for count in range(2 * count + 1):
        print("*", end="")
    print()


for count in range(rows - 2, -1, -1):
    for _ in range(rows - count - 1):
        print(" ", end="")

    for _ in range(2 * count + 1):
        print("*", end="")

    print()