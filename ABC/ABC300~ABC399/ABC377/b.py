N = 8
S = [list(input()) for _ in range(N)]
A = [[0] * 8 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            for k in range(N):
                A[i][k] += 1
            for m in range(N):
                A[m][j] += 1
ans = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            ans += 1
print(ans)
