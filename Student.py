'''
Sample Student class to use in class as a demonstration about how to use classes in Python
'''
__author__ = 'Julian Cochran'
__version__ = '02.08.2024'

class Student:
    def __init__(self, first, last, age, grade, advisor, hometown):
        self.first = first
        self.last= last
        self.age = int(age)
        self.grade = int(grade)
        self.advisor = advisor
        self.hometown = hometown

    def __str__(self):
        return f"{self.last}, {self.first}, age: {self.age}, grade: {self.grade}"