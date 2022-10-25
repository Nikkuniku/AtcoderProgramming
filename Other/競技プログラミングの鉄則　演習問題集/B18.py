N, S = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for s in range(S+1):
        dp[i+1][s] |= dp[i][s]
        if s-a[i] >= 0:
            dp[i+1][s] |= dp[i][s-a[i]]

if not dp[N][S]:
    print(-1)
    exit()

i = N
j = S
ans = []
while i > 0 and j > 0:
    if dp[i-1][j]:
        pass
    elif dp[i-1][j-a[i-1]]:
        ans.append(i)
        j -= a[i-1]
    i -= 1
print(len(ans))
print(*ans[::-1])
