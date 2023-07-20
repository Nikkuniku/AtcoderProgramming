N, Q = map(int, input().split())
condition = [list(map(int, input().split())) for _ in range(Q)]
ans = 1
MOD = 10**9 + 7
for i in range(60):
    tmp = 0
    for j in range(1 << N):
        isOK = True
        for x, y, z, w in condition:
            p = (1 & (j >> (x-1))) | (1 & (j >> (y-1))) | (1 & (j >> (z-1)))
            q = 1 & (w >> i)
            if p != q:
                isOK = False
        if isOK:
            tmp += 1
    ans *= tmp
    ans %= MOD
print(ans)
