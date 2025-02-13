def f(d, s, X):
    dp = [[[0] * 10 for _ in range(2)] for _ in range(d + 1)]
    dp[0][0][0] = 1
    n = str(X)
    for i in range(d):
        if i == 0:
            dp[i + 1][s < int(n[i])][s] = 1
            continue
        for smaller in range(2):
            if smaller == 1:
                L = s
            else:
                L = min(int(n[i]) + 1, s)
            for x in range(s + 1):
                for y in range(L):
                    dp[i + 1][smaller | (y < int(n[i]))][y] += dp[i][smaller][x]
    return sum(dp[d][0]) + sum(dp[d][1])


def g(x):
    k = x
    digit = 0
    res = 0
    init = int(str(x)[0])
    while k > 0:
        digit += 1
        k //= 10
    for d in range(2, digit + 1):
        if d < digit:
            for s in range(1, 10):
                l = pow(10, d) - 1
                res += f(d, s, l)
        else:
            for s in range(1, init + 1):
                res += f(d, s, x)
    return res


L, R = map(int, input().split())
ans = g(R) - g(L - 1)
print(ans)
