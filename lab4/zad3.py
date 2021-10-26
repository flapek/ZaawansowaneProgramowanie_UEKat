class Property:
    def __init__(self, area: int, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, fence: int):
        super().__init__(area, rooms, price, address)
        self.fence = fence
    def __str__(self) -> str:
        return f'House area {self.area}m2, numbers of rooms {self.rooms}, fence size {self.fence}, price {self.price}, address {self.address}.'

class Flat(Property):
    def __init__(self, area: int, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self) -> str:
        return f'Flat area {self.area}m2, numbers of rooms {self.rooms}, floor {self.floor}, price {self.price}, address {self.address}.'


flat = Flat(45, 3, 300000, 'Katowcie, Piłsudzkiego 200/45', 4)
house = House(120, 6, 5500000, 'Katowcie, Piłsudzkiego 1', 100)

print(flat)
print(house)