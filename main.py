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

    def __init__(self,  name: str, city: str, post_code: str,
                        phone_number: str, company_size: str):
        self.__name = name
        self.__city = city
        self.__post_code = post_code
        self.__phone_number = phone_number
        self.__company_size = company_size

    def __str__(self)  -> str:
        return f"Firma {self.__name}, położona w {self.__city} \
            {self.__post_code}, numer kontaktowy \
                {self.__phone_number}. Wielokość \
                    firmy {self.__company_size}."


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

    @property
    def to_company(self) -> Firma:
        return self.__to_company

    @property
    def from_company(self) -> Firma:
        return self.__from_company

    def __init__(self, from_place: str, to_place: str,
                        distance: float, to_company: Firma,
                        from_company: Firma):
        self.__from_place = from_place
        self.__to_place = to_place
        self.__distance = distance
        self.__to_company = to_company
        self.__from_company = from_company

    def __str__(self) -> str:
        return f"Z {self.__from_place} do {self.__to_place}. Dlugość odcinka \
            {self.__distance}, z firmy \
                {self.__to_company} do firmy\
                     pojazdu {self.__from_company}."


class Pojazd:
    @property
    def marka(self) -> str:
        return self.__marka

    @property
    def moc(self) -> int:
        return self.__moc

    @property
    def ilosc_miejsc(self) -> int:
        return self.__ilosc_miejsc

    @property
    def ladownosc(self) -> float:
        return self.__ladownosc

    @property
    def wysokosc_samochodu(self) -> float:
        return self.__wysokosc_samochodu

    def __init__(self, marka: str, moc: int, ilosc_miejsc: int, ladownosc: float, 
                        wysokosc_samochodu: float):
        self.__marka = marka
        self.__moc = moc
        self.__ilosc_miejsc = ilosc_miejsc
        self.__ladownosc = ladownosc
        self.__wysokosc_samochodu = wysokosc_samochodu

    def __str__(self) -> str:
        return f"Marka samochodu {self.marka}, ilość miejsc \
            {self.ilosc_miejsc}, moc {self.moc}, ladowność \
                {self.ladownosc}t, wysokość samochodu \
                    {self.wysokosc_samochodu}"


class Kurs:
    @property
    def odcinki(self) -> list[Odcinek]:
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, value: list[Odcinek]) -> None:
        self.__odcinki = value

    @property
    def id_kierowcy(self) -> str:
        return self.__id_kierowcy

    @id_kierowcy.setter
    def id_kierowcy(self, value: int) -> None:
        self.__id_kierowcy = value

    @property
    def vechicle(self) -> Pojazd:
        return self.__vechicle

    @vechicle.setter
    def vechicle(self, value: Pojazd) -> None:
        self.__vechicle = value

    @property
    def max_vechicle_height(self) -> float:
        return self.__max_vechicle_height

    @max_vechicle_height.setter
    def max_vechicle_height(self, value: float) -> None:
        self.__max_vechicle_height = value

    @property
    def max_vechicle_weight(self) -> float:
        return self.__max_vechicle_weight

    @max_vechicle_weight.setter
    def max_vechicle_weight(self, value: float) -> None:
        self.__max_vechicle_weight = value

    def full_distace(self) -> float:
        result = 0.0
        for odcinek in self.odcinki:
            result += odcinek.distance
        return round(result, 2)

    def marka_samochodu(self) -> str:
        return self.__vechicle.marka

    def __str__(self) -> str:
        result = ""
        for odcinek in self.__odcinki:
            result += f"{odcinek}"
        return f"{result} {self.__id_kierowcy} {self.__vechicle} {self.__max_vechicle_weight}, {self.__max_vechicle_height}"


class FirmaTransportowa(Firma):
    def __init__ (self, name: str, city: str, post_code: str, phone_number: str, company_size: str):
        super().__init__(name, city, post_code, phone_number, company_size)


class FirmaSpożywcza(Firma):
    def __init__ (self, name: str, city: str, post_code: str, phone_number: str, company_size: str):
        super().__init__( name, city, post_code, phone_number, company_size)

firma_transportowa = FirmaTransportowa("Trans", "Warszawa", "43-213", "111 111 111", "big")
firma_spozywcza = FirmaSpożywcza("pan marchweka", "wrocław", "43-111", "222 222 222", "big")
firma_spozywcza2= FirmaSpożywcza("pan truskawka", "katowice", "43-235", "333 333 333", "big")
kurs = Kurs()
kurs.id_kierowcy = 1
kurs.odcinki = [ Odcinek("Warszawa", "Katowice", "124.2", firma_spozywcza, firma_spozywcza2) ]
kurs.vechicle = Pojazd("Seat", 100, 3, 10, 3.5)
kurs.max_vechicle_weight = 13
kurs.max_vechicle_height = 4

print(kurs)
