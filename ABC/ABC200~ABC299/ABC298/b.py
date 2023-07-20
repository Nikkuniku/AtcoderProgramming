N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

ans = 'No'
for _ in range(4):
    C = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = A[N-1-j][i]
    f = True
    for i in range(N):
        for j in range(N):
            if C[i][j] == 1 and C[i][j] != B[i][j]:
                f = False
    if f:
        ans = 'Yes'
    A = C

print(ans)
