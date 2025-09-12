class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)
    
def calculate_average_marks(students):
    average_marks_dict = {}
    for student in students:
        average_marks_dict[student.name] = round(student.average_marks(), 2)
    return average_marks_dict

def find_top_performer(students):
    top_student = max(students, key=lambda student: student.average_marks())
    return top_student.name

students_data = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

students = [Student(name, marks) for name, marks in students_data.items()]
average_marks = calculate_average_marks(students)
top_performer = find_top_performer(students)

print("Average Marks:", average_marks)
print("Top Performer:", top_performer)