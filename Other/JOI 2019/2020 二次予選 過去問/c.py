N = int(input())


def digit_sum(n):
    return sum(list(map(int, str(n))))


dp = [1]*(N+1)
for i in range(1, N+1):
    d = digit_sum(i)
    if i+d > N:
        continue
    dp[i+d] += dp[i]
print(dp[N])
