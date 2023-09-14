#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

def sort_students(students):
    students.sort(key=lambda student: student.cgpa, reverse=True)
  
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("John", "A001", 3.8),
    Student("Jane", "A002", 3.5),
    Student("Alice", "A003", 3.9),
    Student("Bob", "A004", 3.2),
]

sort_students(students)

for student in students:
    print(student.name, student.roll_number, student.cgpa)