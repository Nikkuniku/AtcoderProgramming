from collections import defaultdict, deque

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
Edge_Label = [defaultdict(list) for _ in range(N)]
ans = [[-1] * N for _ in range(N)]
q = deque()
for i in range(N):
    ans[i][i] = 0
    q.append((i, i))
for _ in range(M):
    a, b, c = input().split()
    a = int(a) - 1
    b = int(b) - 1
    Edge[a].append((b, c))
    Edge[b].append((a, c))
    Edge_Label[a][c].append(b)
    Edge_Label[b][c].append(a)
    if a != b:
        ans[a][b] = ans[b][a] = 1
        q.append((a, b))
        q.append((b, a))
while q:
    x, y = q.popleft()
    for to, lab in Edge[x]:
        for to2 in Edge_Label[y][lab]:
            if ans[to][to2] != -1:
                continue
            ans[to][to2] = ans[x][y] + 2
            q.append((to, to2))
print(ans[0][N - 1])
