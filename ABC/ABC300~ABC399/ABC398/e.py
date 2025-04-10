from collections import deque

N = int(input())
Edge = [[-1] * N for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u][v] = Edge[v][u] = 1
colors = [-1] * N
colors[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    for e in range(N):
        if Edge[v][e] == 1 and colors[e] == -1:
            colors[e] = 1 - colors[v]
            q.append(e)
S = set()
for i in range(N):
    for j in range(i + 1, N):
        if colors[i] != colors[j] and Edge[i][j] == -1:
            S.add((i + 1, j + 1))
turn = True
if len(S) % 2 == 0:
    turn = False
if turn:
    print("First")
    print(*S.pop(), flush=True)
else:
    print("Second")
while 1:
    i, j = map(int, input().split())
    if i == -1 and j == -1:
        exit()
    S.discard((i, j))
    print(*S.pop(), flush=True)
