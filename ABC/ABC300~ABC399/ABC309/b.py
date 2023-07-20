N = int(input())
A = [list(input()) for _ in range(N)]
B = [[-1]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0:
            if j < N-1:
                B[i][j+1] = A[i][j]
            else:
                B[i+1][j] = A[i][j]
        elif i == N-1:
            if 0 < j:
                B[i][j-1] = A[i][j]
            else:
                B[i-1][j] = A[i][j]
        else:
            if j == 0:
                B[i-1][j] = A[i][j]
            elif j == N-1:
                B[i+1][j] = A[i][j]
            else:
                B[i][j] = A[i][j]
for c in B:
    print(*c, sep="")
