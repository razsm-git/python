words = input("Введите несколько слов через пробел: ")
for count, value in enumerate(words.split(), start=1):
    if len(value) > 10:
        value = str(value[0:10])
    print(count, value)