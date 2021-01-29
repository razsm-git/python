def func_sum(x=int(input("Введите первый аргумент: ")), y=int(input("Введите второй аргумент: ")),
             z=int(input("Введите третий аргумент: "))):
    result = x + y + z - min(x, y, z)
    print(f'Сумма двух наибольших аргументов: {result}')


func_sum()
