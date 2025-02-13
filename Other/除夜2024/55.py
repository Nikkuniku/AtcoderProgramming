N = 8
S = [list(input()) for _ in range(N)]
res = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            for k in range(N):
                res[i][k] = 1
                res[k][j] = 1
ans = 0
for i in range(N):
    for j in range(N):
        if res[i][j] == 0:
            ans += 1
print(ans)
