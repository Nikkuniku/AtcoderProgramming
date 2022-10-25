N, A, B = map(int, input().split())
X = list(map(int, input().split()))
dp = [[False]*A for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(A):
        dp[i+1][j] |= dp[i][j]
        dp[i+1][(j+X[i]) % A] |= dp[i][j]
ans = 'No'
if dp[N][B]:
    ans = 'Yes'
print(ans)
