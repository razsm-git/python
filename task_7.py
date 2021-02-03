# первый варинат решения
from math import factorial


def my_func(x):
    return factorial(x)


num = int(input('Введите значение для расчета факториала: '))
if num == 0:
    print(f"{num}! = 1")
else:
    for i in range(1, num + 1):
        print(f'{i}! = {my_func(i)}')

print('*' * 45)


# второй варинат решения

def gen_fact(n):
    fact_num = 1
    if n == 0:
        yield f"{n}! = {fact_num}"
    else:
        for i in range(1, n + 1):
            fact_num = fact_num * i
            yield f'{i}! = {fact_num}'


for i in gen_fact(int(input('Введите значение для расчета факториала: '))):
    print(i)
