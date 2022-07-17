from math import ceil
n = int(input())
ans = [[0]*n for _ in range(n)]
for i in range(n):
    p = i*n + 1
    j = 0
    while j < n:
        ans[i][j] = p
        p += 1
        j += 2
    j = 1
    while j < n:
        ans[i][j] = p
        p += 1
        j += 2

for v in ans:
    print(*v)
