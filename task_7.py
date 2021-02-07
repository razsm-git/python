import json

with open('text_7.txt', 'r', encoding='utf-8') as org:
    dict_firm = {}
    dict_avg_profit = {}
    while True:
        var = org.readline()
        if var == '':
            break
        else:
            var = var.split()
            profit = int(var[2]) - int(var[3])
            dict_firm[var[1] + ' ' + var[0]] = int(profit)
    temp_profit = 0
    count_firms = 0
    for i in dict_firm:
        if dict_firm[i] > 0:
            temp_profit = temp_profit + dict_firm[i]
            count_firms += 1
    avg_profit = temp_profit / count_firms
    dict_avg_profit['average_profit'] = avg_profit
    result = [dict_firm, dict_avg_profit]
    print(result)
with open('text_7.json', 'w', encoding='utf-8') as json_f:
    json.dump(result, json_f, ensure_ascii=False)
