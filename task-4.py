N = int(input())
total = 0

if N >= 1:
    for i in range(1, N + 1):
        total += i
else:
    for i in range(1, N - 1, -1):
        total += i

print(total)
