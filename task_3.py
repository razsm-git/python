class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    num = input("Введите число: ")
    if num == 'stop':
        break
    else:
        try:
            num = int(num)
            my_list.append(num)
        except ValueError as err:
            print(f'{MyException("Вы ввели не число")}: {err}')
print(my_list)
