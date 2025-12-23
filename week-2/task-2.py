a = input().strip()
b = input().strip()

s = len(b)
count = 0

shifts = set()
for i in range(len(b)):
    shifts.add(b[i:] + b[:i])

for i in range(len(a) - s + 1):
    if a[i:i+s] in shifts:
        count += 1

print(count)
