from models.Budynek import Budynek


class Dom(Budynek):
    @property
    def posiada_garaz(self) -> bool:
        return self._posiada_garaz

    def __init__(
        self,
        id: int,
        powierzchnia: int,
        ilosc_pokoi: int,
        cena: int,
        posiada_garaz: bool,
    ):
        super().__init__(id, powierzchnia, ilosc_pokoi, cena)
        self._posiada_garaz = posiada_garaz

    def __str__(self) -> str:
        return f"{super().__str__()}, posiada garaz {self._posiada_garaz}"
