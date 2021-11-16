from models.Property import Property


class House(Property):
    @property
    def fence(self) -> None:
        return self._fence

    def __init__(self, area: int, rooms: int, price: float, address: str, fence: int):
        super().__init__(area, rooms, price, address)
        self._fence = fence

    def __str__(self) -> str:
        return f"House area {self._area}m2, numbers of rooms \
            {self._rooms}, fence size {self._fence}, \
                price {self._price}, address {self._address}."
