class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


x = input("Введите положительное число: ")
y = input("Введите второе положительное число: ")

try:
    x = int(x)
    y = int(y)
    if y == 0:
        raise MyException("На ноль делить нельзя")
    else:
        result = x / y
except ValueError:
    print("Вы ввели не число")
except MyException as err:
    print(err)
else:
    print(f'Операция деления завершена. Результат {result}')
finally:
    print('Программа завершила работу')
