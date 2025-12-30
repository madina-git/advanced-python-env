a, b = map(int, input().split()) #уникальные подстроки 
s = input().strip()

sub = set()
for i in range(a - b + 1): # предел
    sub.add(s[i:i+b]) # считаешь все уникальные 1:4

print(len(sub)) # вывлдишь все уникальные подстроки которые в sub
3 