for row in range(len(picture)):
    for column in range(len(picture[row])):
        if (picture[row][column] == 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")
