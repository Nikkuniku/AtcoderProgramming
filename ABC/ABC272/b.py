from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(int)
for _ in range(m):
    p = list(map(int, input().split()))
    k = p[0]
    q = sorted(p[1:])
    for i in range(k):
        for j in range(i+1, k):
            d[(q[i], q[j])] += 1

ans = 'Yes'
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if d[(i, j)] == 0:
            ans = 'No'
            break
print(ans)
