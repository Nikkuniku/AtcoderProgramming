N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    res = []
    for j in range(N):
        if A[i][j] == 1:
            res.append(j + 1)
    print(*res)
