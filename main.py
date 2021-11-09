class Firma:
    @property
    def name(self) -> str:
        return self.__name

    @property
    def city(self) -> str:
        return self.__city

    @property
    def post_code(self) -> str:
        return self.__post_code
        
    @property
    def phone_number(self) -> str:
        return self.__phone_number
        
    @property
    def company_size(self) -> str:
        return self.__company_size

    def __init__(self,  name: str, city: str, post_code: str, phone_number: str, company_size: str):
        self.__name = name
        self.__city = city
        self.__post_code = post_code
        self.__phone_number = phone_number
        self.__company_size = company_size

    def __str__ (self)  -> str:
        return f"Firma {self.__name}, położona w {self.__city} {self.__post_code}, \
            numer kontaktowy {self.__phone_number}. Wielokość firmy {self.__company_size}."


class Odcinek:
    @property
    def from_place(self) -> str:
        return self.__from_place
        
    @property
    def to_place(self) -> str:
        return self.__to_place

    @property
    def distance(self) -> float:
        return self.__distance

    def __init__(self, from_place: str, to_place: str, distance: float):
        self.__from_place = from_place
        self.__to_place = to_place
        self.distance = distance


class Kurs:
    @property
    def odcinki(self) -> list[Odcinek]:
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, value: list[Odcinek]) -> None:
        self.__odcinki = value


    @property
    def kierowca(self) -> str:
        return self.__kierowca

    @kierowca.setter
    def kierowca(self, value: str) -> None:
        self.__kierowca = value


class Pojazd:
    pass

class FirmaTransportowa(Firma):
    def __init__ (self):
        Firma.__init__(self)


class FirmaSpożywcza(Firma):
    def __init__ (self):
        Firma.__init__(self)


