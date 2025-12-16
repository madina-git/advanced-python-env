A = int(input())
total = 0

if A >= 1:
    for i in range(1, A + 1):
        total += i
else:
    for i in range(1, A - 1, -1):
        total += i

print(total)
