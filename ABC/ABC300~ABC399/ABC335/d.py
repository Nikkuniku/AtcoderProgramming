N = int(input())
ans = [[-1] * N for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
now = 1
now_dir = 0
x, y = 0, 0
while now < N * N:
    ans[x][y] = now
    now += 1
    x += direction[now_dir][0]
    y += direction[now_dir][1]
    if not (0 <= x < N and 0 <= y < N):
        x -= direction[now_dir][0]
        y -= direction[now_dir][1]
        now_dir += 1
        now_dir %= 4
        x += direction[now_dir][0]
        y += direction[now_dir][1]
    if (0 <= x < N and 0 <= y < N) and ans[x][y] != -1:
        x -= direction[now_dir][0]
        y -= direction[now_dir][1]
        now_dir += 1
        now_dir %= 4
        x += direction[now_dir][0]
        y += direction[now_dir][1]
ans[(N) // 2][(N) // 2] = "T"
for c in ans:
    print(*c)
