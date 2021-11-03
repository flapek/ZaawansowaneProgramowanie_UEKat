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


class House(Property):
    @property
    def fence(self) -> None:
        return self._fence

    def __init__(self, area: int, rooms: int, price: float,
                 address: str, fence: int):
        super().__init__(area, rooms, price, address)
        self._fence = fence

    def __str__(self) -> str:
        return f'House area {self._area}m2, numbers of rooms \
            {self._rooms}, fence size {self._fence}, \
                price {self._price}, address {self._address}.'


class Flat(Property):
    @property
    def floor(self) -> None:
        return self._floor

    def __init__(self, area: int, rooms: int, price: float,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return f'Flat area {self._area}m2, numbers of rooms {self._rooms}, \
            floor {self._floor}, price {self._price}, address {self._address}.'


flat = Flat(45, 3, 300000, 'Katowcie, Piłsudzkiego 200/45', 4)
house = House(120, 6, 5500000, 'Katowcie, Piłsudzkiego 1', 100)
print(flat)
print(house)
