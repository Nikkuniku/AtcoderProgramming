N, M = map(int, input().split())
A = list(map(int, input().split()))
kakutei = [0] * M
ans = [-1] * N
T = [list(map(int, input().split())) for _ in range(N)]
for j in range(M):
    for i in range(N):
        if ans[i] != -1:
            continue
        t = T[i][j]
        if kakutei[t] < A[t]:
            ans[i] = t
            kakutei[t] += 1
print(*ans)
