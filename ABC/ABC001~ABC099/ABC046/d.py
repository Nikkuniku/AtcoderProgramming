from collections import Counter
s = input()
c = Counter(s)
g = c['g']
p = c['p']

ans = (g-p)//2
if g < p:
    ans = (p-g)//2
print(ans)
