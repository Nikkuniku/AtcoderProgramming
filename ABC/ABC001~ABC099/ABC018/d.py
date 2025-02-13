from itertools import combinations

N, M, P, Q, R = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(R)]
comb = combinations([i for i in range(N)], P)
ans = 0
for c in comb:
    binary = 0
    for p in c:
        binary |= 1 << p
    val = [0] * M
    for x, y, z in C:
        x -= 1
        y -= 1
        if binary & (1 << x):
            val[y] += z
    val.sort(reverse=True)
    ans = max(ans, sum(val[:Q]))
print(ans)
