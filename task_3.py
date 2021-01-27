print("Через list")
user_month = int(input("Введите номер месяца: "))
list_month = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь','Июль', 'Август', 'Сентябрь','Октябрь', 'Ноябрь', 'Декабрь')
list_time_of_year = ('Зима', 'Весна', 'Лето', 'Осень')
if 1 <= user_month <= 2 or user_month == 12:
    print(f'Месяц {list_month[user_month - 1]} - это {list_time_of_year[0].lower()}')
elif 3 <= user_month <= 5:
    print(f'Месяц {list_month[user_month - 1]} - это {list_time_of_year[1].lower()}')
elif 6 <= user_month <= 8:
    print(f'Месяц {list_month[user_month - 1]} - это {list_time_of_year[2].lower()}')
else:
    print(f'Месяц {list_month[user_month - 1]} - это {list_time_of_year[3].lower()}')

print('*' * 42)

print("Через dict")
user_month = int(input("Введите номер месяца: "))
dict_month = { 1:'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',7: 'Июль', 8: 'Август', 9: 'Сентябрь',10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
dict_time_of_year = { 1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if 1 <= user_month <= 2 or user_month == 12:
    print(f'Месяц {dict_month[user_month]} - это {dict_time_of_year[1].lower()}')
elif 3 <= user_month <= 5:
    print(f'Месяц {dict_month[user_month]} - это {dict_time_of_year[2].lower()}')
elif 6 <= user_month <= 8:
    print(f'Месяц {dict_month[user_month]} - это {dict_time_of_year[3].lower()}')
else:
    print(f'Месяц {dict_month[user_month]} - это {dict_time_of_year[4].lower()}')