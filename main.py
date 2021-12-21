from models.Developer import Developer
from models.Dom import Dom
from models.Mieszkanie import Mieszkanie
from models.Zamownienie import Zamownienie


developer = Developer(1, "Adam", "Kowaliski", "33")
dom = Dom(1, 130, 5, 300000, 0)
mieszkanie = Mieszkanie(2, 50, 3, 250000, 1)
mieszkanie2 = Mieszkanie(3, 50, 3, 250000, 1)

zamowienie = Zamownienie()
zamowienie.id = 1
zamowienie.data_realizacji = "10 grudani 2022"
zamowienie.id_developera = 1
zamowienie.lista_budynkow = [dom, mieszkanie, mieszkanie2]

print(zamowienie)
print(f'Cena za zamowienie: {zamowienie.cena()}')
print(f'Ilosc metrow: {zamowienie.metraz()}')
