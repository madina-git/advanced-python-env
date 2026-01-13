def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print("Введите дроби A/B и C/D")

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))


numerator = A * D - C * B
denominator = B * D


g = gcd(abs(numerator), denominator)

numerator //= g
denominator //= g

print("Результат:")
print(numerator, "/", denominator)
