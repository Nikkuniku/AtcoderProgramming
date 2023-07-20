N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 10**18
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            A[i][j] = INF
for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][k] != INF and A[k][j] != INF:
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
ans = []
Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    s %= N
    t %= N
    ans.append((-1 if A[s][t] == INF else A[s][t]))
print(*ans, sep="\n")
