from collections import deque
H, W = map(int, input().split())
S = [['.']*(W+2) for _ in range(H+2)]
for i in range(H):
    S[i+1] = ['.']+list(input())+['.']
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque([(1, 1)])
dist = [[-1]*(W+2) for _ in range(H+2)]
dist[1][1] = 0
d = {"s": "n", "n": "u", "u": "k", "k": "e", "e": "s"}
while q:
    vx, vy = q.popleft()
    if S[vx][vy] not in d:
        continue
    p = d[S[vx][vy]]
    for dx, dy in dxy:
        nx = vx+dx
        ny = vy+dy
        if S[nx][ny] == p and dist[nx][ny] == -1:
            dist[nx][ny] = dist[vx][vy]+1
            q.append((nx, ny))
ans = 'No' if dist[H][W] == -1 else'Yes'
print(ans)
