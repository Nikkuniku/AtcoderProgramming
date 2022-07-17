n, k = map(int, input().split())
a = list(map(int, input().split()))
g = [[] for _ in range(k)]
for i in range(n):
    g[i % k].append(a[i])
for i in range(k):
    g[i].sort(reverse=True)

ans = []
for i in range(n):
    p = g[i % k].pop()
    ans.append(p)
a.sort()
if ans == a:
    print('Yes')
else:
    print('No')
