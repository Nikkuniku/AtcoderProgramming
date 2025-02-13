N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
P.sort(key=lambda x: x[1], reverse=True)
P.sort(key=lambda x: x[0])
px, py = -1, -1
ans = 0
for i in range(N):
    x, y = P[i]
    if i == 0:
        ans += 1
        px, py = x, y
    else:
        if px != x:
            ans += 1
            px, py = x, y
        else:
            if px * y >= (py - 1) * x:
                continue
            else:
                ans += 1
                px, py = x, y
print(ans)
