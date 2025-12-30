text = input("Введите текст: ")

words = text.split()

for w in words:
    print("".join(sorted(w)), end=" ")
