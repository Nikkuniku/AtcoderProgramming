N, K = map(int, input().split())
A = list(map(int, input().split()))
cum = [0]
for p in A:
    cum.append(cum[-1]+p)

l = -1
r = 1 << 10
while r-l > 1:
    mid = (l+r)//2
    dp = [-1]*(N+1)
    dp[0] = 0
    for i in range(N):
        for j in range(i+1):
            if dp[j] != -1 and cum[i+1]-cum[j] >= mid:
                dp[i+1] = max(dp[i+1], dp[j]+1)

    if dp[N] >= K:
        l = mid
    else:
        r = mid
print(l)
