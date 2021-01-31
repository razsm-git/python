def my_func(x, y):
    if x <= 0 or (x is int or x is float):
        print('Первый аргумент должен быть положительным числом!')
    elif y >= 0 or (type(y) is not int):
        print('Второй аргумент должен быть отрицательным целым числом')
    else:
        result = x ** y
        print(result)


my_func(-1.5, 0)
