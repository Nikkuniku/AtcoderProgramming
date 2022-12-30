n = int(input())
a = []
for _ in range(n):
    a.append(list(input()))
ans = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(n):
        for k in range(8):
            tmp = ''
            nx = dx[k]
            ny = dy[k]
            for m in range(n):
                tmp += a[i][j]
                i += nx
                j += ny
                i %= n
                j %= n
            ans = max(ans, int(tmp))
print(ans)
