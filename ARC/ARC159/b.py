
def rec(a, b):
    from math import gcd
    res = 0
    while a > 0 and b > 0:
        g = gcd(a, b)
        a -= g
        b -= g
        res += 1
    return res


A, B = map(int, input().split())
print(rec(A, B))
N = 10
dp = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        dp[i][j] = rec(i+1, j+1)
for c in dp:
    print(*c, )
print(A-B)
