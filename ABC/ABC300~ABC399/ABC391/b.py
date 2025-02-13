N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]
for a in range(N - M + 1):
    for b in range(N - M + 1):
        isOK = True
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    isOK = False
                    break
        if isOK:
            exit(print(a + 1, b + 1))
