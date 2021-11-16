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

    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str,
    ):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"Library is located in {self._city} \
            (zip code {self._zip_code}) on the street {self._street}. \
                Open houers {self._open_hours}, phone number {self._phone}."
