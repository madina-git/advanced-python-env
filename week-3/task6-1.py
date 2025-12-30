# функция для НОД по алгоритму Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        # после каждой итерации a становится b, а b — остатком
    return a


# ввод чисел
A = int(input("A = "))
B = int(input("B = "))

# находим НОД
g = gcd(A, B)

# находим НОК по формуле
lcm = (A * B) // g

print("GCD =", g)
print("LCM =", lcm)
