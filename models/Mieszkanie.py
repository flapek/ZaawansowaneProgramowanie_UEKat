from models.Budynek import Budynek


class Mieszkanie(Budynek):
    @property
    def pietro(self) -> int:
        return self._pietro

    def __init__(
        self,
        id: int,
        powierzchnia: int,
        ilosc_pokoi: int,
        cena: int,
        pietro: int,
    ):
        super().__init__(id, powierzchnia, ilosc_pokoi, cena)
        self._pietro = pietro

    def __str__(self) -> str:
        return f"{super().__str__()}, pietro {self.pietro}"
