N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
ans = []
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for dx, dy in dxy:
    nx = cx + dx
    ny = cy + dy
    if not (1 <= nx <= N and 1 <= ny <= N):
        continue
    ans.append((nx, ny))
print(len(ans))
for c in ans:
    print(*c)
