numbers = list(map(int, input("Введите числа через пробел: ").split()))

s = sum(numbers)
avg = s / len(numbers)

print("сумма =", s)
print("среднее =", avg)
