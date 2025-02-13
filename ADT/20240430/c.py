N = int(input())
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i + 1):
        if j == 0 or j == i:
            ans[i][j] = 1
        else:
            if i > 0:
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
for i in range(N):
    print(*ans[i][: (i + 1)])
