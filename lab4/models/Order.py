from models.Book import Book
from models.Student import Student
from models.Employee import Employee

class Order:
    @property
    def employee(self) -> None:
        return self._employee

    @property
    def student(self) -> None:
        return self._student

    @property
    def books(self) -> None:
        return self._books

    @property
    def order_date(self) -> None:
        return self._order_date

    def __init__(self, employee: Employee, student: Student,
                 books: "list[Book]", order_date: str):
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        result = f'Employee taking the order\n{self._employee}\n\
            from {self._student}\non books'
        for book in self._books:
            result = result + f'\n- {book}'
        result = result + f'. Order date {self._order_date}.\n\n'
        return result
