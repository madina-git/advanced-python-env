# функция нахождения НОД (алгоритм Евклида)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("Введите дроби A/B и C/D")

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

# числитель и знаменатель после вычитания
numerator = A * D - C * B
denominator = B * D

# находим НОД
g = gcd(abs(numerator), denominator)

# сокращаем дробь
numerator //= g
denominator //= g

print("Результат:")
print(numerator, "/", denominator)
