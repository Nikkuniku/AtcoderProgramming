M, N = map(int, input().split())
K = int(input())
Planet = [[[0]*N for _ in range(M)] for _ in range(3)]
d = {'J': 0, 'O': 1, 'I': 2}
for i in range(M):
    S = input()
    for j in range(N):
        Planet[d[S[j]]][i][j] = 1
for i in range(M):
    for j in range(N-1):
        Planet[0][i][j+1] += Planet[0][i][j]
        Planet[1][i][j+1] += Planet[1][i][j]
        Planet[2][i][j+1] += Planet[2][i][j]
for i in range(M-1):
    for j in range(N):
        Planet[0][i+1][j] += Planet[0][i][j]
        Planet[1][i+1][j] += Planet[1][i][j]
        Planet[2][i+1][j] += Planet[2][i][j]
ans = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    tmp = []
    for k in range(3):
        res = Planet[k][c][d]
        if b > 0:
            res -= Planet[k][c][b-1]
        if a > 0:
            res -= Planet[k][a-1][d]
        if a > 0 and b > 0:
            res += Planet[k][a-1][b-1]
        tmp.append(res)
    ans.append(tmp)
for c in ans:
    print(*c)
