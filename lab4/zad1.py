class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50


student1 = Student(name="Student", marks=50)
student2 = Student(name="Student", marks=59)

print(f'Student1 zdał {student1.is_passed()}')
print(f'Student2 zdał {student2.is_passed()}')
