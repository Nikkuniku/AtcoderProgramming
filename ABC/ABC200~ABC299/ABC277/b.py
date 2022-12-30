from collections import defaultdict
n = int(input())
a = list('HDCS')
b = list('A23456789TJQK')
d = defaultdict(int)
ans = 'Yes'
for _ in range(n):
    s = input()
    if s[0] in a and s[1] in b:
        d[s] += 1
    else:
        ans = 'No'

for key, value in d.items():
    if value >= 2:
        ans = 'No'
print(ans)
