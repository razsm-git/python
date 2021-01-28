goods = [(1, {'Имя товара': "", 'Цена': "", 'Кол-во': "", 'Ед.измерения': ""}),
         (2, {'Имя товара': "", 'Цена': "", 'Кол-во': "", 'Ед.измерения': ""}),
         (3, {'Имя товара': "", 'Цена': "", 'Кол-во': "", 'Ед.измерения': ""})]
name = input('Введите имя товара(можно указать несколько значений через пробел): ').split()
price = input('Введите стоимость товара(можно указать несколько значений через пробел): ').split()
count = input('Введите кол-во товара(можно указать несколько значений через пробел): ').split()
var = input('Введите ед. измерения товара(можно указать несколько значений через пробел): ').split()
index_1 = 0
n_1 = 0
for i in name:
    if len(name) > 1:
        goods[index_1][1]['Имя товара'] = name[n_1]
        index_1 += 1
        n_1 += 1
    if len(name) == 1:
        goods[0][1]['Имя товара'] = name[0]
index_2 = 0
n_2 = 0
for i in price:
    if len(price) > 1:
        goods[index_2][1]['Цена'] = price[n_2]
        index_2 += 1
        n_2 += 1
    if len(price) == 1:
        goods[0][1]['Цена'] = price[0]
index_4 = 0
n_4 = 0
for i in count:
    if len(count) > 1:
        goods[index_4][1]['Кол-во'] = count[n_4]
        index_4 += 1
        n_4 += 1
    if len(count) == 1:
        goods[0][1]['Кол-во'] = count[0]
index_5 = 0
n_5 = 0
for i in var:
    if len(var) > 1:
        goods[index_5][1]['Ед.измерения'] = var[n_5]
        index_5 += 1
        n_5 += 1
    if len(var) == 1:
        goods[0][1]['Ед.измерения'] = var[0]
if (len(name) or len(price) or len(count) or len(var)) == 1:
    print(goods[0])
elif (len(name) or len(price) or len(count) or len(var)) == 2:
    print(goods[0], goods[1], sep='\n')
elif (len(name) or len(price) or len(count) or len(var)) == 3:
    print(goods[0], goods[1], goods[2], sep='\n')
# Аналитика товаров
print('Аналитика:')
analitic_name = {'Имя товара': [goods[0][1]['Имя товара'], goods[1][1]['Имя товара'], goods[2][1]['Имя товара']]}
analitic_price = {'Цена': [goods[0][1]['Цена'], goods[1][1]['Цена'], goods[2][1]['Цена']]}
analitic_count = {'Кол-во': [goods[0][1]['Кол-во'], goods[1][1]['Кол-во'], goods[2][1]['Кол-во']]}
analitic_var = {'Ед.измерения': [goods[0][1]['Ед.измерения'], goods[1][1]['Ед.измерения'], goods[2][1]['Ед.измерения']]}
print(analitic_name, analitic_price, analitic_count, analitic_var, sep='\n')
