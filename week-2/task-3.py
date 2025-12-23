equation = input().strip()

a, op, b, _, c = equation

if a == 'x':
    a = int(c) - int(b) if op == '+' else int(c) + int(b)
elif b == 'x':
    b = int(c) - int(a) if op == '+' else int(a) - int(c)
else:
    c = int(a) + int(b) if op == '+' else int(a) - int(b)
    print(c)
    exit()

print(a if isinstance(a, int) else b)
