with open('text_4.txt', 'r', encoding='utf-8') as txt:
    count_lines = 0
    for line in txt:
        count_lines += 1
        count_words = 0
        line = line.split()
        for w in line:
            count_words += 1
        print(f'Кол-во слов в строке {count_lines} равно: {count_words}')
