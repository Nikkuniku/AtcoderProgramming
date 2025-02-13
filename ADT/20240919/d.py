N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        px, py = P[i]
        qx, qy = P[j]
        tmp = (px - qx) ** 2 + (py - qy) ** 2
        ans = max(ans, tmp**0.5)
print(ans)
