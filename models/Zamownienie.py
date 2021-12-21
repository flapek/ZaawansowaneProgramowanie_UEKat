from models.Budynek import Budynek


class Zamownienie:
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def data_realizacji(self) -> int:
        return self._data_realizacji

    @data_realizacji.setter
    def data_realizacji(self, data_realizacji: int):
        self._data_realizacji = data_realizacji

    @property
    def id_developera(self) -> int:
        return self._id_developera

    @id_developera.setter
    def id_developera(self, id_developera: int):
        self._id_developera = id_developera

    @property
    def lista_budynkow(self) -> list():
        return self._lista_budynkow

    @lista_budynkow.setter
    def lista_budynkow(self, lista_budynkow: list()):
        self._lista_budynkow = lista_budynkow

    def cena(self) -> int:
        return sum([item.cena for item in self._lista_budynkow])

    def metraz(self) -> int:
        return sum([item.powierzchnia for item in self._lista_budynkow])

    def __str__(self) -> str:
        return f"Id {self._id}, data_realizacji {self._data_realizacji}, \
            id developera {self._id_developera}, lista budynkow \
                {[item.id for item in self._lista_budynkow]}"
