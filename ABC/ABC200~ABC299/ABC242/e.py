
def ceil(a, b):
    return -(-a//b)


def alp(s):
    return ord(s)-65


def solve(N, S):
    M = ceil(N, 2)
    dp = [[0, 0] for _ in range(M+1)]
    dp[0][0] = 1
    for i in range(M):
        num = alp(S[i])
        for smaller in range(2):
            limit = 26 if smaller else num+1
            for x in range(limit):
                dp[i+1][smaller | (x < num)] += dp[i][smaller]
                dp[i+1][smaller | (x < num)] %= MOD
    ans = sum(dp[M]) % MOD
    if N % 2 == 0:
        palindrom = S[:M]+S[:M][::-1]
    else:
        palindrom = S[:M-1]+S[M-1]+S[:M-1][::-1]
    if palindrom > S:
        ans -= 1
        ans %= MOD
    return ans


ans = []
T = int(input())
MOD = 998244353
for _ in range(T):
    N = int(input())
    S = input()
    ans.append(solve(N, S))
print(*ans, sep="\n")
