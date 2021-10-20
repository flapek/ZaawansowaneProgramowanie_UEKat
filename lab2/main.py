# Zadanie 2a
def printNames(names):
    for name in names:
        print(name)

names = ["martin", "alex", "gloria", "melman", "szeregowy"]

print("--------------------")
print("Zadanie 2a")
printNames(names)

# Zadanie 2b i
def multiply(numbers):
    result = []
    for i in numbers:
        result.append(numbers[i - 1] * 2)
    return result

numbers1 = [1, 2, 3, 4, 5]
copyOfNumbers1 = multiply(numbers1)

print("--------------------")
print("Zadanie 2b i")
print(numbers1)
print(copyOfNumbers1)

# Zadanie 2b ii
def multiply2(numbers):
    return [value * 2 for value in numbers]

numbers2 = [1, 2, 3, 4, 5]
copyOfNumbers2 = multiply2(numbers2)

print("--------------------")
print("Zadanie 2b ii")
print(numbers2)
print(copyOfNumbers2)


# Zadanie 2b ii
def multiply2(numbers):
    return [value * 2 for value in numbers]

numbers3 = [1, 2, 3, 4, 5]
copyOfNumbers3 = multiply2(numbers3)

print("--------------------")
print("Zadanie 2b ii")
print(numbers3)
print(copyOfNumbers3)


# Zadanie 2c
def onlyEven(numbers):
    result = []
    for i in numbers:
        if numbers[i - 1] % 2 == 0:
            result.append(numbers[i - 1])
    return result

numbers4 = range(10)
copyOfNumbers4 = onlyEven(numbers4)

print("--------------------")
print("Zadanie 2c")
print(numbers4)
print(copyOfNumbers4)

# Zadanie 2d
def everySecondNumber(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(numbers[i - 1])
    return result

numbers5 = range(20)
copyOfNumbers5 = everySecondNumber(numbers5)

print("--------------------")
print("Zadanie 2d")
print(numbers5)
print(copyOfNumbers5)