# Zadanie 1
def string_createGreatings(name: str, surname: str) -> str:
    return f'Czesc {name} {surname}!'


greattings: str = string_createGreatings('Marcin', 'Nowak')
print('Zadanie 1')
print(greattings)
print('--------------------------')


# Zadanie 2
def int_multiply(a: int, b: int) -> int:
    return a*b


print('Zadanie 2')
print(int_multiply(10, 3))
print('--------------------------')


# Zadanie 3
def bool_isEven(a: int) -> bool:
    return a % 2 == 0


even = 10
odd = 9
print('Zadanie 3')
print(f"Liczba parzysta {even}") if bool_isEven(10) else \
    print(f"Liczba nieparzysta {even}")
print(f"Liczba parzysta {odd}") if bool_isEven(9) else \
    print(f"Liczba nieparzysta {odd}")
print('--------------------------')


# Zadanie 4
def bool_CompareNumbers(a: int, b: int, c: int) -> bool:
    return a + b >= c


print('Zadanie 4')
print(f'A = 10, B = 2, C = 12. A + B >= C is {bool_CompareNumbers(10,2,12)}')
print('--------------------------')


# Zadanie 5
def bool_checkNumber(listOfNumbers: list[int], valueToCheck: int) -> bool:
    return valueToCheck in listOfNumbers


listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print('Zadanie 5')
print('List of numbers', listOfNumbers)
print(f'A = 10 exist in list of numbers: \
    {bool_checkNumber(listOfNumbers, 10)}')
print('--------------------------')


# Zadanie 6
def set_mergeList(firstList: list, secondList: list) -> set:
    return set(firstList + secondList)


def set_exponentiation(firstList: set) -> set:
    return [value ** 3 for value in firstList]


def set_removeDuplicatesAndMagnify(firstList: list, secondList: list) -> set:
    return set_exponentiation(set_mergeList(firstList, secondList))


firstList = [1, 2, 3, 4, 5, 6]
secondList = [1, 2, 3, 4, 5]

print('Zadanie 6')
print('First list of numbers', firstList)
print('Second list of numbers', secondList)
print(f'Output list: {set_removeDuplicatesAndMagnify(firstList, secondList)}')
print('--------------------------')
