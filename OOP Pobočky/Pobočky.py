class Position:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def change_position(self, new_position):
        self.position.remove_employee(self)
        self.position = new_position
        self.position.add_employee(self)

class Branch:
    all_branches = [] 
    def __init__(self, name):
        self.name = name
        self.positions = []
        self.employees = []
        Branch.all_branches.append(self)

    def add_position(self, position):
        self.positions.append(position)

    def remove_position(self, position):
        self.positions.remove(position)

    def show_positions(self):
        for position in self.positions:
            print(f"Pozice v pobočce {self.name} je: {position.name}")

    def show_employees(self):
        for position in self.positions:
            print(f"Zaměstnanci na pozici {position.name} v pobočce {self.name}")
            for employee in position.employees:
                print(f"- {employee.name}")

    @classmethod
    def show_branches(cls):
        print("Vytvořené pobočky: ")
        for branch in cls.all_branches:
            print(f"- {branch.name}")

def create_branch():
    branch_name = input("Zadejte název pobočky: ")
    return Branch(branch_name)

def create_position():
    position_name = input("Zadej název pozice: ")
    return Position(position_name)

def create_employee():
    employee_name = input("Zadej jméno zaměstnance: ")
    return Employee(employee_name, None)

branch = None

while True:
    print("1 - Přidat pobočku")
    print("2 - Odstranit pobočku")
    print("3 - Přidat pozici")
    print("4 - Odstranit pozici")
    print("5 - Přidat zaměstnance")
    print("6 - Odstranit zaměstnance")
    print("7 - Zobrazit pozice")
    print("8 - Zobrazit zaměstnance")
    print("9 - Zobrazit pobočky")
    print("0 - Konec")

    choose = input("Vyber číslo akce: ")

    if choose == "1":
        branch = create_branch()
        print(f"Byla vytvořena pobočka '{branch.name}'.")
    elif choose == "2":
        branch_name = input("Zadejte název pobočky kterou chcete odstranit: ")
        for branch in Branch.all_branches:
            if branch.name == branch_name:
                Branch.all_branches.remove(branch)
                print(f"Pobočka '{branch_name}' byla odstraněna.")
                break
        else:
            print("Pobočka nebyla nalezena.")
    elif choose == "3":
        position = create_position()
        branch.add_position(position)
        print(f"Pozice '{position.name}' byla vytvořena v pobočce '{branch.name}'.")
    elif choose == "4":
        position_name = input("Zadejte název pozice kterou chcete odstranit: ")
        for position in branch.positions:
            if position.name == position_name:
                branch.remove_position(position)
                print(f"Pozice '{position_name}' byla odstraněna z pobočky '{branch.name}'.")
                break
        else:
            print("Pozice nebyla nalezena.")
    elif choose == "5":
        employee = create_employee()
        position_name = input("Zadejte název pozice pro zaměstance: ")
        for position in branch.positions:
            if position.name == position_name:
                position.add_employee(employee)
                print(f"Zaměstnanec '{employee.name}' byl přidán na pozici '{position_name}' v pobočce '{branch.name}'.")
                break
    elif choose == "6":
        employee_name = input("Zadej jméno zaměstnance k vyhození z pobočky: ")
        for position in branch.positions:
            for employee in position.employees:
                if employee.name == employee_name:
                    position.remove_employee(employee)
                    print(f"Zaměstnanec '{employee_name}' byl vyhozen z pobočky '{branch.name}'.")
                    break
            else:
                print("Zaměstnanec nebyl nalezen.")
                break
        else:
            print("Pozice nebyla nalezena.")
    elif choose == "7":
        branch.show_positions()
    elif choose == "8":
        branch.show_employees()
    elif choose == "9":
        Branch.show_branches()
    elif choose == "0":
        break