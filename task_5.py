from functools import reduce


def my_func(x, y):
    # x - первый аргумент, y - следующий
    return x * y


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, my_list))
