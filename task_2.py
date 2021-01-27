count_of_list = int(input("Введите кол-во элементов списка: "))
first_list = []
for i in range(count_of_list):
    val = input("Введите значение элемента списка: ")
    first_list.append(val)
long_list = len(first_list)
item_of_list = 0
while long_list > item_of_list + 1:
    first_list[item_of_list], first_list[item_of_list + 1] = first_list[item_of_list + 1], first_list[item_of_list]
    item_of_list += 2
print(first_list)
