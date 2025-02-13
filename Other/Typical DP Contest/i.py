S = input()
N = len(S)
removable = [[False] * (N + 1) for _ in range(N + 1)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    removable[i][i] = True
for k in range(1, N + 1):
    for l in range(N):
        r = l + k
        if r > N:
            continue
        for m in range(l, r):
            if S[l] == "i" and S[m] == "w" and S[r - 1] == "i":
                if removable[l + 1][m] and removable[m + 1][r - 1]:
                    removable[l][r] = True
            if removable[l][m] and removable[m][r]:
                removable[l][r] = True
for l in range(N):
    for r in range(N):
        if removable[l][r]:
            dp[l][r] = r - l
ans = 0
ep = [0] * (N + 1)  # ep[k]=[0,k)
tmp = 0
for r in range(1, N):
    tmp = max(tmp, dp[0][r])
    ep[r] = max(tmp, ep[r])
for m in range(N):
    ans = max(ans, ep[m] + dp[m][N])
print(ans)
