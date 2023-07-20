def solve(K):
    MOD = 998244353
    res = 0
    for y in range(1, K+1):
        if y*y > K:
            break
        res += 6*(y-1)*((K//y)-y)
        res += 3*((K//y)-y)
        res += 3*(y-1)
        res += 1
        res %= MOD
    return res


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    ans.append(solve(N))
print(*ans, sep="\n")
