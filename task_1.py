def my_func(x=int(input('Введите значениме x: ')), y=int(input('Введите значениме y: '))):
    if y != 0:
        result = f'Частное: {(x / y):.1f}'
    elif y == 0:
        try:
            result = x / y
        except ZeroDivisionError:
            result = "На ноль делить нельзя!"
    return result


print(my_func())
