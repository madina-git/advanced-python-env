n = int(input("Введите число: "))

if n == 0:
    octal = "0"
else:
    octal = ""
    while n > 0:
        digit = n % 8
        octal = str(digit) + octal
        n //= 8

octal = octal.zfill(10)

print(octal)
