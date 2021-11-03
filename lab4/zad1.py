class Student:
    @property
    def name(self) -> None:
        return self._name

    @property
    def marks(self) -> None:
        return self._marks

    def __init__(self, name: str, marks: int):
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return self._marks > 50


student1 = Student(name="Student", marks=50)
student2 = Student(name="Student", marks=59)
print(f'Student1 zdał {student1.is_passed()}')
print(f'Student2 zdał {student2.is_passed()}')
