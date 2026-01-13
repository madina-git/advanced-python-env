import math


def heron(a, b, c):
    p = (a + b + c) / 2          # полупериметр
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print("Введите 4 стороны четырёхугольника и диагональ")

a = float(input("Сторона 1: "))
b = float(input("Сторона 2: "))
c = float(input("Сторона 3: "))
d = float(input("Сторона 4: "))
diag = float(input("Диагональ: "))


s1 = heron(a, b, diag)


s2 = heron(c, d, diag)


S = s1 + s2

print("Площадь четырёхугольника =", S)
