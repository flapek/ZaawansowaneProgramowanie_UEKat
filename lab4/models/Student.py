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

    def __str__(self) -> str:
        return f'Student name: {self._name}. Student mark: {self._marks}%'