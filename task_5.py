from random import randint

with open('file_5.txt', 'w', encoding='utf-8') as num:
    my_list = [randint(-10, 20) for _ in range(20)]
    for i in my_list:
        var = str(i) + ' '
        num.write(var)
with open('file_5.txt', 'r', encoding='utf-8') as num_2:
    temp = num_2.read().split()
    result = 0
    for x in temp:
        result = result + int(x)
    print(f'Сумма числе в файле: {result}')
