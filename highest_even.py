def highest_even(input_list):
    output_list = []
    for num in input_list:
        if (num % 2 == 0):
            output_list.append(num)
    output_list.sort()
    return output_list.pop()


print((highest_even([10, 2, 3, 4, 8, 11, 8, 12, 22, 23, 26, 2, 4, 8, 13])))
