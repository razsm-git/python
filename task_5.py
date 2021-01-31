def func_sum():
    var = 0
    while True:
        number = input('Введите последовательность чисел через пробел: ').split()
        for i in number:
            if i == 'q':
                return print(f'Сумма введенных чисел {var}')
            else:
                try:
                    var = var + int(i)
                except ValueError:
                    print("Для завершения программы введите 'q'")
        print(f'Сумма введенных чисел {var}')


func_sum()
