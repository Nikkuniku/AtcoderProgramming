n, k = map(int, input().split())
a = list(map(lambda x: int(x)-1, input().split()))
next = [[0]*n for _ in range(61)]
for i in range(n):
    next[0][i] = a[i]
for d in range(60):
    for i in range(n):
        next[d+1][i] = next[d][next[d][i]]
ans = 0
for i in range(60):
    if k & (1 << i):
        ans = next[i][ans]
print(ans+1)
