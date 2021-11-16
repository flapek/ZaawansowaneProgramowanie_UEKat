from models.Student import Student
from models.Library import Library
from models.Employee import Employee
from models.Book import Book
from models.Order import Order

employee1 = Employee(
    "Jacek",
    "Nowak",
    "10.02.2021",
    "11.01.1990",
    "Katowice",
    "Czysta 125/1",
    "43-200",
    "+48 923 111 234",
)
employee2 = Employee(
    "Franciszek",
    "Kowalski",
    "10.05.2010",
    "11.01.1990",
    "Wrocaław",
    "Wyzwolenia 125/1",
    "43-311",
    "+48 888 222 234",
)
employee3 = Employee(
    "Adam",
    "Nowak",
    "12.02.2018",
    "11.05.1980",
    "Warszawa",
    "Wyzwolenia 1/1",
    "43-891",
    "+48 111 111 111",
)
student1 = Student("Artur", 50)
student2 = Student("Grzegorz", 59)
student3 = Student("Jacek", 100)
library1 = Library(
    "Katowice", "Słowackiego 100/5", "43-200", "9-17", "+48 222 222 222"
)
library2 = Library(
    "Warszawa", "Słowackiego 100/5", "43-891", "9-18", "+48 333 333 333"
)
book1 = Book(library1, "10.01.2018", "Krychowiak", "", 102)
book2 = Book(library1, "10.04.2016", "Andrzej", "Błasik", 70)
book3 = Book(library2, "10.04.2019", "Grzegorz", "Nowy", 102)
book4 = Book(library2, "10.01.2017", "Ewa", "Nowak", 102)
book5 = Book(library2, "01.12.2010", "Krychowiak", "", 102)
order1 = Order(employee1, student1, [book1], "25.10.2021")
order2 = Order(employee2, student3, [book4, book5, book3], "25.10.2021")
print(f"Order 1:\n{order1}")
print(f"Order 2:\n{order2}")
