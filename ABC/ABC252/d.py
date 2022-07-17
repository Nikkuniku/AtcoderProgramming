from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
ans = n*(n-1)*(n-2)//6
t = list(c.values())
for v in list(c.values()):
    p = 0
    q = 0
    if v >= 2:
        p = v*(v-1)*(n-v)//2
    if v >= 3:
        q = v*(v-1)*(v-2)//6
    ans -= p
    ans -= q
print(ans)
