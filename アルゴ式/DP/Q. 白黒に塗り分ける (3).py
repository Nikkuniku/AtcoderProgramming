M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
INF = 1 << 30
dp = [[[INF]*(1 << M) for _ in range(1 << M)] for _ in range(N)]


def check(arr):
    p = len(arr)
    q = len(arr[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(p):
        for j in range(q):
            if arr[i][j] == '1':
                continue
            tmp = 0
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if 0 <= ni < p and 0 <= nj < q:
                    if arr[ni][nj] == '0':
                        tmp += 1
            if tmp > 2:
                return False
    return True


def isOK(p, bit1, bit2):
    # i列目
    for j in range(M):
        whitecnt = 0
        if p & (1 << j):
            continue
        if j < M-1 and p & (1 << (j+1)) == 0:
            whitecnt += 1
        if 0 < j and p & (1 << (j-1)) == 0:
            whitecnt += 1
        if bit1 & (1 << j) == 0:
            whitecnt += 1
        if whitecnt > 2:
            return False
     # i-1列目
    for j in range(M):
        whitecnt = 0
        if bit1 & (1 << j):
            continue
        if j < M-1 and bit1 & (1 << (j+1)) == 0:
            whitecnt += 1
        if 0 < j and bit1 & (1 << (j-1)) == 0:
            whitecnt += 1
        if bit2 & (1 << j) == 0:
            whitecnt += 1
        if p & (1 << j) == 0:
            whitecnt += 1
        if whitecnt > 2:
            return False
    return True


sum_Acol = [[0 for _ in range(1 << M)] for _ in range(N)]
for i in range(N):
    for p in range(1 << M):
        for k in range(M):
            if p & (1 << k):
                sum_Acol[i][p] += A[k][i]

full = (1 << M)-1
for i in range(N):
    if i == 0:
        for j in range(1 << M):
            if isOK(j, full, full):
                for m in range(1 << M):
                    dp[i][j][m] = sum_Acol[i][j]
    elif i == 1:
        for j in range(1 << M):
            for m in range(1 << M):
                if isOK(j, m, full):
                    res = sum_Acol[i][j]+sum_Acol[i-1][m]
                    dp[i][j][m] = min(dp[i][j][m], res)
    else:
        for j in range(1 << M):
            for m in range(1 << M):
                for r in range(1 << M):
                    if isOK(j, m, r):
                        dp[i][j][m] = min(dp[i][j][m],
                                          dp[i-1][m][r]+sum_Acol[i][j])
ans = min(sum(dp[N-1], []))
print(ans)
