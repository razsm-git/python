max_number = 0
current = None
number = int(input("Введите ваше число: "))
while number <= 0:
    number = int(input("Введите положительно число!: "))
while number > 0:
    current = number % 10
    if current > max_number:
        max_number = current
    number = number // 10
print("Максимальное число: ", max_number)
