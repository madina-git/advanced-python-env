a = input().strip()
b = input().strip()

s = len(b) #длина строки b
count = 0

shifts = set()
for i in range(len(b)):
    shifts.add(b[i:] + b[:i])# берем позициии в начале и в конце 

for i in range(len(a) - s + 1): #не выйти за приделы границы строки 
    if a[i:i+s] in shifts: #тут мы берем кусочек от a и сравниваем с b, берем из а s букв поряд начиная с i 
        count += 1

print(count)
