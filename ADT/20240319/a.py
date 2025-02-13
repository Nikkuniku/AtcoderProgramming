H, W = map(int, input().split())
R, C = map(int, input().split())
R -= 1
C -= 1
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
for dx, dy in dxy:
    ni = R + dx
    nj = C + dy
    if 0 <= ni < H and 0 <= nj < W:
        ans += 1
print(ans)
