class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"cash": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print('Доход сотудника составляет: {}'.format(self._income['cash'] + self._income['bonus']))


a = Position("Иван", "Иванов", "слесарь", 25000, 10000)
a.get_full_name()
a.get_total_income()
