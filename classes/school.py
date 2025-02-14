# school.py
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = []