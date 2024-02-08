'''
An example of how to use objects in Python in a list, we will expand on this to make a dictionary
'''
__author__ = 'Julian Cochran'
__version__ = '02.08.2024'

from Student import *

students = []
students.append(Student('Garrett', 'Zhou', 14, 9, 'Evans', 'Chapel Hill'))
students.append(Student('Natalie', 'McWhorter', 15, 9, 'Loch', 'Durham'))
students.append(Student('Ganapathi', 'Pamula', 15, 9, 'Monahan', 'Cary'))
students.append(Student('Marco', 'Gullotto', 15, 10, 'Mahajan', 'Raleigh'))
students.append(Student('Luis', 'Pastor-Valverde', 17, 11, 'Meyer', 'Durham'))
students.append(Student('Maya', 'Goldstein', 14, 9, 'Brookhart', 'Chapel Hill'))

print('students as added')
for student in students:
    print(student)

students.sort(key=lambda student: student.age, reverse=False)
print('students sorted by last name')
for student in students:
    print(student)