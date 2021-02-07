first_file = open('text.txt', 'a', encoding='utf-8')
while True:
    user = input('Введите слово/слова: ')
    if user == '':
        break
    else:
        user = user.split()
        for i in user:
            content = first_file.write(i+'\n')
first_file.close()
with open('text.txt', 'r', encoding='utf-8') as my_text:
    for line in my_text:
        print(line, end='')
