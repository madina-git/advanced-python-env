n = int(input("Введите n: "))

for i in range(1, n + 1):
    s = str(i)
    ok = True

    for d in s:
        if d == '0':
            ok = False
            break
        if i % int(d) != 0:
            ok = False
            break

    if ok:
        print(i, end=" ")
