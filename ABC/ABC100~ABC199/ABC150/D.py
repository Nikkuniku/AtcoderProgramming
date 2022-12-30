from math import gcd


def lcm(a, b):
    return a*b//gcd(a, b)


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i]//2 for i in range(N)]

X = 1
for i in range(N):
    X = lcm(X, B[i])
s = set()
for i in range(N):
    tmp = B[i]
    cnt = 0
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    s.add(cnt)
Diff = 1
for i in range(N):
    Diff = lcm(Diff, A[i])


ans = max(0, 1 + ((M-X)//Diff))
if len(s) > 1:
    ans = 0
print(ans)
