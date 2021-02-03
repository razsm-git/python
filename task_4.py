from random import randint

list_numbers = [randint(0, 12) for i in range(25)]
print(f'Исходный список: {list_numbers}, уникальные значения:',
      new_list := [n for n in list_numbers if list_numbers.count(n) == 1])
