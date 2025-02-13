N = int(input())
S = [list(input()) for _ in range(N)]
M = max([len(s) for s in S])
T = [["*"] * N for _ in range(M)]
for j in range(M):
    for i in range(N):
        if len(S[i]) <= j:
            continue
        T[j][i] = S[i][j]
for j in range(M):
    T[j] = T[j][::-1]
    while T[j][-1] == "*":
        T[j].pop()
for c in T:
    print(*c, sep="")
