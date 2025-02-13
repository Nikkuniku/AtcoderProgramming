N = int(input())
A = []
B = []
tot = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    tot += a
ans = 0
for i in range(N):
    tmp = tot - A[i] + B[i]
    ans = max(ans, tmp)
print(ans)
