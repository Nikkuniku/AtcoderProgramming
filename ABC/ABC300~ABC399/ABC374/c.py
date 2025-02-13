N = int(input())
K = list(map(int, input().split()))
S = sum(K)
ans = 1e18
for i in range(1 << N):
    a = 0
    for j in range(N):
        if i & (1 << j):
            a += K[j]
    b = S - a
    tmp = max(a, b)
    ans = min(ans, tmp)
print(ans)
