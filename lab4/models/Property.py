class Property:
    @property
    def area(self) -> None:
        return self._area

    @property
    def rooms(self) -> None:
        return self._rooms

    @property
    def price(self) -> None:
        return self._price

    @property
    def address(self) -> None:
        return self._address

    def __init__(self, area: int, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address
