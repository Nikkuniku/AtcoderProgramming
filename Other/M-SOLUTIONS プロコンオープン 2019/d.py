from collections import deque
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
c = list(map(int, input().split()))
c = sorted(c)[::-1]
ans = [-1]*n
q = deque([0])
c = deque(c)
while q:
    v = q.popleft()
    ans[v] = c.popleft()
    for e in edge[v]:
        if ans[e] != -1:
            continue
        q.append(e)

print(sum(ans)-max(ans))
print(*ans)
