from models.Property import Property


class Flat(Property):
    @property
    def floor(self) -> None:
        return self._floor

    def __init__(self, area: int, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return f"Flat area {self._area}m2, numbers of rooms {self._rooms}, \
            floor {self._floor}, price {self._price}, address {self._address}."
