n = int(input())
A = list(map(int, input().split()))

dp = [0]*(1 << n)
for s in range(1 << n):
    tmp = 0
    for c in range(n):
        if (s >> c) & 1:
            tmp += 1
    if tmp % 2 == 1:
        continue

    for a in range(n):
        if s & (1 << a) == 0:
            for b in range(a+1, n):
                if s & (1 << b) == 0:
                    if dp[s | ((1 << a) | (1 << b))] < dp[s]+ (A[a] ^ A[b]):
                        dp[s | ((1 << a) | (1 << b))] = dp[s]+(A[a] ^ A[b])

print(dp[(1 << n)-1])
