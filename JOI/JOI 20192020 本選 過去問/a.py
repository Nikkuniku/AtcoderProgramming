N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_ind = [(A[i], i) for i in range(N+1)]
A.sort()
A_ind.sort()
B.sort()
dp = [max(A[i]-B[i], 0) for i in range(N)]
ep = [max(A[i+1]-B[i], 0) for i in range(N)]
for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1])
    ep[N-1-i] = max(ep[N-1-i], ep[N-i])
ans = [0]*(N+1)
for i in range(N+1):
    _, j = A_ind[i]
    if i == 0:
        ans[j] = ep[i]
    elif i == N:
        ans[j] = dp[i-1]
    else:
        ans[j] = max(dp[i-1], ep[i])
print(*ans)
