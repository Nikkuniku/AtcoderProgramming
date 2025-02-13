x1, y1, x2, y2 = map(int, input().split())
dxy = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
P = set()
Q = set()
for dx, dy in dxy:
    nx = x1 + dx
    ny = y1 + dy
    mx = x2 + dx
    my = y2 + dy
    P.add((nx, ny))
    Q.add((mx, my))
ans = "Yes" if len(P & Q) > 0 else "No"
print(ans)
