my_student = {
    'name':'Rolf Smith',
    'grades': [70,88,90,99]
}

def average_grade(student):
    return sum(student['grades'])/ len(student['grades'])

class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades)/len(self.grades)
    
student_one = Student()