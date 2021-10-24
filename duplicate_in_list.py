some_list = [1, 2, 3, 4, 4, 5, 6, 6, 8, 8, 9, 10]
result_list = []

for item in some_list:
    if some_list.count(item) > 1:
        result_list.append(item)
print((result_list))
