list_of_number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_of_number[i] for i in range(1, len(list_of_number)) if list_of_number[i] > list_of_number[i-1]]
print(new_list)