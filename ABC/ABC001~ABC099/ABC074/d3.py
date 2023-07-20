from copy import deepcopy
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = deepcopy(A)

for u in range(N):
    for v in range(N):
        for w in range(N):
            B[u][v] = min(B[u][v], B[u][w]+B[w][v])
if A != B:
    print(-1)
    exit()
ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans += A[i][j]
for u in range(N):
    for v in range(u+1, N):
        for w in range(N):
            if w == u or w == v:
                continue
            if A[u][w]+A[w][v] == A[u][v]:
                ans -= A[u][v]
                break

print(ans)
