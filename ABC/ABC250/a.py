h, w = map(int, input().split())
r, c = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0
for k in range(4):
    nr = r+dx[k]
    nc = c+dy[k]
    if 1 <= nr <= h and 1 <= nc <= w:
        ans += 1
print(ans)
