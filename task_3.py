with open('text_3.txt', 'r', encoding='utf-8') as payment:
    cash = 0
    count_workers = 0
    poor = []
    for line in payment:
        line = line.split()
        count_workers += 1
        # my_dict = {line[0]: line[1] for i in line}
        if float(line[1]) < 20000:
            poor.append(line[0])
        cash = cash + float(line[1])
avg_cash = cash / count_workers
print(f"Сотрудники, чей оклад менее 20000 рублей: {poor}, средняя величина дохода: {avg_cash} рублей.")
