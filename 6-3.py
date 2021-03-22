class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return  f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum( self._income.values())}"

engineer = Position("Ivan", "Sidorov", "Chemical", 50000, 10000)
print(engineer.get_full_name())
print(engineer.position)
print(engineer.get_full_profit())
