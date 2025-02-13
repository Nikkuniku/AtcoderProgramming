N, K = map(int, input().split())
A = [list(input()) for _ in range(N)]
ans = [["."] * (N * K) for _ in range(N * K)]
for i in range(N):
    for j in range(N):
        si = K * i
        sj = K * j
        for x in range(K):
            for y in range(K):
                ans[si + x][sj + y] = A[i][j]
for c in ans:
    print(*c, sep="")
