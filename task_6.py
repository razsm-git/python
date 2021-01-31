def int_func():
    words = input("Введите слово: ").title()
    return words


print(int_func())

'*' * 45


def int_func2():
    words = input("Введите слова через пробел(латинскими маленькими буквами): ").split()
    for word in words:
        var = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                var += 1
        print(word.title() if var == len(word) else f"Слово {word} должно быть написнао маленькими латинскими буквами")


int_func2()
