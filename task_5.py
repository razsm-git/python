proceeds = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if proceeds > costs:
    profit = proceeds - costs
    print("Ваша фирма в плюсе, прибыль составляет", profit)
    profitability = profit / proceeds
    print(f"Рентабельность фирмы: {profitability:.2f}")
    workers = int(input("Введите кол-во сотрудников фирмы: "))
    profit_per_worker = profit / workers
    print("Прибыль в расчёте на одного сотрудника составляет: ", profit_per_worker)
elif proceeds == costs:
    print("Баланс фирмы нулевой")
else:
    profit = costs - proceeds
    print("Ваша фирма в минусе, убыток составляет", profit)
