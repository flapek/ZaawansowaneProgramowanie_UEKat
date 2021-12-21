class Budynek:
    @property
    def id(self) -> int:
        return self._id

    @property
    def powierzchnia(self) -> int:
        return self._powierzchania

    @property
    def ilosc_pokoi(self) -> int:
        return self._ilosc_pokoi

    @property
    def cena(self) -> int:
        return self._cena

    def __init__(
        self, id: int, powierzchnia: int, ilosc_pokoi: int, cena: int
    ):
        self._id = id
        self._powierzchania = powierzchnia
        self._ilosc_pokoi = ilosc_pokoi
        self._cena = cena

    def __str__(self) -> str:
        return f"Id {self._id}, powierzchnia {self._powierzchania}, \
            ilosc_pokoi {self._ilosc_pokoi}, cena {self.cena} tys. zł"
