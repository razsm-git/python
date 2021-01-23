day1 = int(input("Введите кол-во км, которое пробегает спортсмен сейчас: "))
day2 = int(input("Введите кол-во км, которое хочет пробегать спортсмен: "))
current = day1
i = 1
while current < day2:
    current = current + current * 0.1
    i += 1
result = "Спортсмен пробежит расстояние {} км не менее чем на {} день".format(day2, i)
print(result)
