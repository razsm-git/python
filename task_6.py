# итератор, генерирующий целые числа, начиная с указанного
from itertools import count
from itertools import cycle

start_num = int(input('Введите число для старта: '))
for i in count(start_num):
    if i > 20:
        break
    else:
        print(i)

print('*' * 45)
# итератор, повторяющий элементы некоторого списка, определенного заранее

n = 0
for el in cycle(['macos', 'windows', 'linux']):
    if n > 5:
        break
    else:
        print(el.title())
        n += 1
