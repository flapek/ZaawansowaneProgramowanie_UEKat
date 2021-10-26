class Student: 
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self) -> str:
        return f'Student name: {self.name}. Student mark: {self.marks}%'

class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Library is located in {self.city} (zip code {self.zip_code}) on the street {self.street}. Open houers {self.open_hours}, phone number {self.phone}.'
   
class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date =hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone 

    def __str__(self) -> str:
        return f'Employee data: \n- first name: {self.first_name}, \n- last name: {self.last_name}, \n- hire date: {self.hire_date}, \n- birth date: {self.birth_date}, \n- city: {self.city}, \n- street: {self.street}, \n- zip code: {self.zip_code}, \n- phone: {self.phone},'
    
class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name 
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    
    def __str__(self) -> str:
        return f'Book is located in library: {self.library}. Book information:\n- publication date: {self.publication_date}\n- author name: {self.author_name}\n- author surname: {self.author_surname}\n- number of pages: {self.number_of_pages}'

class Order:
    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
    def __str__(self) -> str:
        result = f'Employee taking the order\n{self.employee}\nfrom {self.student}\non books'
        for book in self.books:
            result = result + f'\n- {book}'
        result = result + f'. Order date {self.order_date}.\n\n'
        return result

employee1 = Employee('Jacek', 'Nowak', '10.02.2021', '11.01.1990', 'Katowice', 'Czysta 125/1', '43-200', '+48 923 111 234')
employee2 = Employee('Franciszek', 'Kowalski', '10.05.2010', '11.01.1990', 'Wrocaław', 'Wyzwolenia 125/1', '43-311', '+48 888 222 234')
employee3 = Employee('Adam', 'Nowak', '12.02.2018', '11.05.1980', 'Warszawa', 'Wyzwolenia 1/1', '43-891', '+48 111 111 111')

student1 = Student("Artur", 50)
student2 = Student("Grzegorz", 59)
student3 = Student("Jacek", 100)

library1 = Library('Katowice', 'Słowackiego 100/5', '43-200', '9-17', '+48 222 222 222')
library2 = Library('Warszawa', 'Słowackiego 100/5', '43-891', '9-18', '+48 333 333 333')

book1 = Book(library1, '10.01.2018', 'Krychowiak', '', 102)
book2 = Book(library1, '10.04.2016', 'Andrzej', 'Błasik', 70)
book3 = Book(library2, '10.04.2019', 'Grzegorz', 'Nowy', 102)
book4 = Book(library2, '10.01.2017', 'Ewa', 'Nowak', 102)
book5 = Book(library2, '01.12.2010', 'Krychowiak', '', 102)

order1 = Order(employee1, student1, [book1], '25.10.2021')
order2 = Order(employee2, student3, [book4, book5, book3], '25.10.2021')

print(f'Order 1:\n{order1}')
print(f'Order 2:\n{order2}')
