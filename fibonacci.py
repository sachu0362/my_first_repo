# def fib(terms):
#     first_num = 0
#     second_num = 1
#     next_num = 0
#     print(first_num)
#     print(second_num)
#     for i in range(terms-1):
#         next_num = first_num + second_num
#         first_num = second_num
#         second_num = next_num
#         print(next_num)

# def fib(terms):
#     first_num = 0
#     second_num = 1
#     next_num = 0
#     series = [first_num,second_num]
#
#     for i in range(terms-1):
#         next_num = first_num + second_num
#         first_num = second_num
#         second_num = next_num
#         series.append(next_num)
#     print(series)



def fib(terms):
    first_num = 0
    second_num = 1
    for i in range(terms-1):
        yield (first_num)
        temp = first_num
        first_num = second_num
        second_num = temp + second_num



for i in fib(20):
    print(i)