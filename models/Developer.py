class Developer:
    @property
    def id(self) -> str:
        return self._id

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def wiek(self) -> int:
        return self._wiek

    def __init__(
        self,
        id: str,
        imie: str,
        nazwisko: str,
        wiek: int,
    ):
        self._id = id
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def __str__(self) -> str:
        return f"Id: {self._id}, imie: {self._imie}, \
            Nazwisko: {self._nazwisko}, wiek: {self._wiek}"
