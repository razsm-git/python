my_list = [8, 5, 3, 3, 2]
print(f'Текущий рейтинг {my_list}')
user_var = int(input("Введите новый элемент рейтинга: "))
if user_var > max(my_list):
    my_list.insert(0, user_var)
elif user_var < min(my_list):
    my_list.append(user_var)
elif my_list.count(user_var):
    index = 0
    list_of_index = []
    for i in my_list:
        if user_var == i:
            list_of_index.append(index)
        index += 1
    my_list.insert(max(list_of_index) + 1, str(user_var))
#В условии не указано, что делать с такими числами, поэтому поступлю на своёусмотрение
else:
    my_list.append(user_var)
print(my_list)
