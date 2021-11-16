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
                    street: {self._street}, \n- zip code: {self._zip_code}, \n\
                        - phone: {self._phone},'
