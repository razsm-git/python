class DateClass:
    def __init__(self, date):
        self.date = date

    n = []

    def __str__(self):
        d = str(self.date).split('.')
        for i in d:
            i = int(i)
            DateClass.n.append(i)
        return f'{DateClass.n}'

    @staticmethod
    def get_date():
        if 0 <= DateClass.n[0] > 31:
            print('Введено неверное число!')
        elif 0 <= DateClass.n[1] > 12:
            print('Введен неверный месяц!')
        elif DateClass.n[2] <= 0:
            print('Введен неверный год!')
        else:
            print(f'число: {DateClass.n[0]} месяц: {DateClass.n[1]} год: {DateClass.n[2]}')


a = DateClass('12.01.2012')
print(a)
DateClass.get_date()
