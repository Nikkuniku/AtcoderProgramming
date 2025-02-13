N, K = map(int, input().split())
A = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(N)]
B = set(A)
ans = 0
for i in range(N):
    if i + 1 in B:
        continue
    tmp = 1 << 60
    sx, sy = P[i]
    for j in A:
        j -= 1
        tx, ty = P[j]
        dist = ((sx - tx) ** 2 + (sy - ty) ** 2) ** 0.5
        tmp = min(tmp, dist)
    ans = max(ans, tmp)
print(ans)
