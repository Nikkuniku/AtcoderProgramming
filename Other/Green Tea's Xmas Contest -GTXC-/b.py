from collections import defaultdict
H, W, N = map(int, input().split())
kanban = defaultdict(int)
for _ in range(N):
    h, w, d = input().split()
    h = int(h)-1
    w = int(w)-1
    kanban[(h, w)] = d
grid = [[-1]*W for _ in range(H)]
sx, sy = 0, 0
dir = 'D'
while True:
    grid[sx][sy] = 0
    if kanban[(sx, sy)] != 0:
        dir = kanban[(sx, sy)]
    if dir == 'U':
        sx -= 1
    elif dir == 'D':
        sx += 1
    elif dir == 'R':
        sy += 1
    else:
        sy -= 1
    if not(0 <= sx < H and 0 <= sy < W):
        break
    elif grid[sx][sy] == 0:
        break
ans = []
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if grid[a][b] == 0:
        ans.append('Yes')
    else:
        ans.append('No')
print(*ans, sep="\n")
