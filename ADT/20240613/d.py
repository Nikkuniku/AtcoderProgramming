N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ans = -1
for i in range(N):
    for j in range(i + 1, N):
        ax, ay = P[i]
        bx, by = P[j]
        tmp = ((ax - bx) ** 2 + (ay - by) ** 2) ** (0.5)
        ans = max(tmp, ans)
print(ans)
