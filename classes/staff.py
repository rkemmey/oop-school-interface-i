#staff.py
import csv
from classes.person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

@classmethod
def all_staff(cls):
    container = []
    with open('./data/staff.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_staff = Staff(**row)
            container.append(new_staff)
            #container.append(cls(**row)) # creates an instance of the class
    return container