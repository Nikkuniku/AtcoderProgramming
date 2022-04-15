from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))
d = defaultdict(int)
ope = set()
can = True
for i in range(n):
    d[p[i]] = i
ans = []
for j in range(n, 0, -1):
    if d[j] == j-1:
        continue

    while d[j] != j-1:
        now = d[j]
        d[j] += 1
        d[p[now+1]] -= 1
        p[now], p[now+1] = p[now+1], p[now]
        if now+1 in ope:
            can = False
        ope.add(now+1)
        ans.append(now+1)

    if not can:
        break

if len(ans) != n-1:
    can = False
if can:
    print(*ans, sep="\n")
else:
    print(-1)
