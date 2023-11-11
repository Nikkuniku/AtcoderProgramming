N = int(input())
ans = [[0]*(N+1) for _ in range(N+1)]
ans[0][0] = 1
for i in range(N):
    for j in range(N):
        ans[i+1][j] += ans[i][j]
        ans[i+1][j+1] += ans[i][j]

for i in range(N):
    tmp = []
    for j in range(i+1):
        tmp.append(ans[i][j])
    print(*tmp)
