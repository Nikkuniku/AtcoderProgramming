from collections import deque
N = map(int, input().split())
P = list(map(int, input().split()))
P = deque(P)
pre = 1 << 62
tmp = []
while True:
    a = P.pop()
    tmp.append(a)
    if a < pre:
        pre = a
    else:
        break

# aより小さくて一番大きいものを見つける
m = -1
for p in tmp:
    if p < a:
        m = max(m, p)
tmp.remove(m)
tmp.sort(reverse=True)
res = [m]+tmp
ans = []
if P:
    for p in P:
        ans.append(p)
ans += res
print(*ans)
