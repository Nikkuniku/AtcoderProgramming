from math import gcd
N = int(input())
A = list(map(int, input().split()))
g = 0
for c in A:
    g = gcd(g, c)

ans = 0
for i in range(N):
    can = False
    tmp = 1 << 60
    for j in range(31):
        for k in range(31):
            p = (A[i]//pow(2, j))//pow(3, k)
            if g == p:
                tmp = min(tmp, j+k)
                can = True
    if can:
        ans += tmp
    else:
        ans = -1
        break
print(ans)
