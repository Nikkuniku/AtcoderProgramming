M, N = map(int, input().split())
S = [list(input()) for _ in range(M)]
T = [list(input()) for _ in range(2)]
C = [[0]*(N+1) for _ in range(M+1)]
for i in range(M-1):
    for j in range(N-1):
        isOK = True
        for k in range(2):
            for m in range(2):
                if S[i+k][j+m] != T[k][m]:
                    isOK = False
        if isOK:
            C[i+1][j+1] = 1
for i in range(M+1):
    for j in range(N):
        C[i][j+1] += C[i][j]
for j in range(N+1):
    for i in range(M):
        C[i+1][j] += C[i][j]
ans = 0
dxy = [(-1, -1), (-1, 0), (0, -1), (0, 0)]
for i in range(M):
    for j in range(N):
        pre = S[i][j]
        U = C[M][N]
        Q = C[min(i+1, M)][min(j+1, N)]\
            - C[min(i+1, M)][max(j+1-2, 0)]\
            - C[max(i+1-2, 0)][min(j+1, N)]\
            + C[max(i+1-2, 0)][max(j+1-2, 0)]
        for henkou in ['J', 'O', 'I']:
            if pre == henkou:
                continue
            S[i][j] = henkou
            tmp = 0
            for dx, dy in dxy:
                ni = i+dx
                nj = j+dy
                if not (0 <= ni < M and 0 <= nj < N):
                    continue
                isOK = True
                for k in range(2):
                    for m in range(2):
                        if not (0 <= ni+k < M and 0 <= nj+m < N):
                            isOK = False
                            continue
                        if S[ni+k][nj+m] != T[k][m]:
                            isOK = False
                if isOK:
                    tmp += 1
            ans = max(ans, U-Q+tmp)
        S[i][j] = pre

print(ans)
