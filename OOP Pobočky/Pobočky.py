from turtle import pos


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Position:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_emloyee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

class Branch:
    def __init__(self, name):
        self.name = name
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def remove_position(self, position):
        self.positions.remove(position)

branch = Branch("Pobočka 1")

position = Position("Hlavní Šéf")
position1 = Position("Zástupce Šéfa")

