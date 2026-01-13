c = float(input())
int_part = int(c)
frac_part = c - int_part
result = round(frac_part * 100 + int_part / 100, 2)
print(result)
