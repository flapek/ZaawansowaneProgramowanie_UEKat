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


class Library:
    @property
    def city(self) -> None:
        return self._city

    @property
    def street(self) -> None:
        return self._street

    @property
    def zip_code(self) -> None:
        return self._zip_code

    @property
    def open_hours(self) -> None:
        return self._open_hours

    @property
    def phone(self) -> None:
        return self._phone

    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f'Library is located in {self._city} (zip code {self._zip_code}) \
            on the street {self._street}. Open houers {self._open_hours}, \
                phone number {self._phone}.'


class Employee:
    @property
    def first_name(self) -> None:
        return self._first_name

    @property
    def last_name(self) -> None:
        return self._last_name

    @property
    def hire_date(self) -> None:
        return self._hire_date

    @property
    def birth_date(self) -> None:
        return self._birth_date

    @property
    def city(self) -> None:
        return self._city

    @property
    def zip_code(self) -> None:
        return self._zip_code

    @property
    def phone(self) -> None:
        return self._phone

    def __init__(self, first_name: str, last_name: str, hire_date: str,
                 birth_date: str, city: str, street: str, zip_code: str,
                 phone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f'Employee data: \n- first name: {self._first_name}, \n- last \
            name: {self._last_name}, \n- hire date: {self._hire_date}, \n\
                - birth date: {self._birth_date}, \n- city: {self._city}, \n- \
                    street: {self._street}, \n- zip code: {self._zip_code}, \n- \
                        phone: {self._phone},'


class Book:
    @property
    def library(self) -> None:
        return self._library

    @property
    def publication_date(self) -> None:
        return self._publication_date

    @property
    def author_name(self) -> None:
        return self._author_name

    @property
    def author_surname(self) -> None:
        return self._author_surname

    @property
    def number_of_pages(self) -> None:
        return self._number_of_pages

    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str, number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f'Book is located in library: {self._library}. \
            Book information:\n- publication date: {self._publication_date}\n\
                - author name: {self._author_name}\n- author surname: \
                    {self._author_surname}\n- number of pages: \
                        {self._number_of_pages}'


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


employee1 = Employee('Jacek', 'Nowak', '10.02.2021', '11.01.1990', 'Katowice',
                     'Czysta 125/1', '43-200', '+48 923 111 234')
employee2 = Employee('Franciszek', 'Kowalski', '10.05.2010', '11.01.1990',
                     'Wrocaław', 'Wyzwolenia 125/1', '43-311',
                     '+48 888 222 234')
employee3 = Employee('Adam', 'Nowak', '12.02.2018', '11.05.1980',
                     'Warszawa', 'Wyzwolenia 1/1', '43-891', '+48 111 111 111')

student1 = Student("Artur", 50)
student2 = Student("Grzegorz", 59)
student3 = Student("Jacek", 100)

library1 = Library('Katowice', 'Słowackiego 100/5', '43-200',
                   '9-17', '+48 222 222 222')
library2 = Library('Warszawa', 'Słowackiego 100/5', '43-891',
                   '9-18', '+48 333 333 333')

book1 = Book(library1, '10.01.2018', 'Krychowiak', '', 102)
book2 = Book(library1, '10.04.2016', 'Andrzej', 'Błasik', 70)
book3 = Book(library2, '10.04.2019', 'Grzegorz', 'Nowy', 102)
book4 = Book(library2, '10.01.2017', 'Ewa', 'Nowak', 102)
book5 = Book(library2, '01.12.2010', 'Krychowiak', '', 102)

order1 = Order(employee1, student1, [book1], '25.10.2021')
order2 = Order(employee2, student3, [book4, book5, book3], '25.10.2021')

print(f'Order 1:\n{order1}')
print(f'Order 2:\n{order2}')
