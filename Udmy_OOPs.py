picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# print(len(picture[1]))


# for row in range(len(picture)):
#     for column in range(len(picture[row])):
#         print(picture[row][column],end=" ")
#     print("\n")


for row in range(len(picture)):
    for column in range(len(picture[row])):
        if (picture[row][column] == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")
