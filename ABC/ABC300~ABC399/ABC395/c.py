N = int(input())
A = list(map(int, input().split()))
M = 10**6
B = [[] for _ in range(M + 1)]
for i, a in enumerate(A):
    B[a].append(i)
INF = 1 << 60
ans = INF
for v in range(M + 1):
    if len(B[v]) > 1:
        for j in range(len(B[v]) - 1):
            temp = B[v][j + 1] - B[v][j] + 1
            ans = min(ans, temp)
if ans == INF:
    ans = -1
print(ans)
