my_student = {
    'name':'Rolf Smith',
    'grades': [70,88,90,99],
    'average':None
}

def average_grade(student):
    return sum(student['grades'])/ len(student['grades'])

class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades)/len(self.grades)
    
student_one = Student('Rolf',[70,80,90,100])
student_two = Student('Jose',[50,60,70,80])

print(student_one.name,end=" ")
print(student_one.average())
print(student_two.name,end=" ")

print(student_two.average())
