from collections import defaultdict

N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
d = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    d[x] = y
now = 1
while now < N:
    T += d[now]
    if T - A[now] > 0:
        T -= A[now]
        now += 1
    else:
        break
ans = "Yes" if now == N else "No"
print(ans)
