n, m = map(int, input().split())
s = input().strip()

sub = set()
for i in range(n - m + 1):
    sub.add(s[i:i+m])

print(len(sub))
