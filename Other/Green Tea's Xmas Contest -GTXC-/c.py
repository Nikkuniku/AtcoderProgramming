from math import gcd
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Diff = [abs(A[i]-B[i]) for i in range(N)]
g = 0
for c in Diff:
    g = gcd(g, c)
ans = 0
if g > 0:
    for d in Diff:
        ans += d//g
print(ans)
