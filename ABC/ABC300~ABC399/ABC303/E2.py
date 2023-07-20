N = int(input())
deg = [0]*N
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    deg[u] += 1
    deg[v] += 1
ans = []
C = N
for i in range(N):
    if deg[i] >= 3:
        C -= deg[i]+1
        ans.append(deg[i])
for _ in range(C//3):
    ans.append(2)
ans.sort()
print(*ans)
